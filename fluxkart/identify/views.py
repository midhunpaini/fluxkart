from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from django.db.models import Q

class IdentifyView(APIView):
    def post(self, request):
        email = request.data.get('email')
        phoneNumber = request.data.get('phoneNumber')

        # Find existing contacts with the same email or phoneNumber
        
        contacts = Contact.objects.filter(Q(email=email) | Q(phoneNumber=phoneNumber))
        print(contacts)
        if contacts.exists():
            current_contact = contacts.order_by('createdAt').first()
            linked_id = current_contact.linkedId or current_contact.id
            primary_contact = Contact.objects.filter(id=linked_id)
            linked_contacts = Contact.objects.filter(linkedId=linked_id)
            contacts = contacts | linked_contacts | primary_contact
            print(contacts)
            dup_primary_contacts = contacts.filter(linkPrecedence='primary')
            if dup_primary_contacts.count() > 1:
                dup_primary = dup_primary_contacts.order_by('createdAt').last()
                dup_primary.linkPrecedence = 'secondary'
                dup_primary.linkedId = contacts.order_by('createdAt').first().id
                dup_primary.save()

            if not Contact.objects.filter(email=email, phoneNumber=phoneNumber).exists() and email and phoneNumber:
                new_contact = Contact.objects.create(email=email, phoneNumber=phoneNumber, linkedId=primary_contact.first().id, linkPrecedence='secondary')
            
            secondary_contacts = Contact.objects.filter(linkedId = primary_contact.first().id)
            secondary_contact_ids = [contact.id for contact in secondary_contacts]
            distinct_phone_numbers = secondary_contacts.exclude(phoneNumber=primary_contact.first().phoneNumber).values_list('phoneNumber', flat=True).distinct()
            distinct_emails = secondary_contacts.exclude(email=primary_contact.first().email).values_list('email', flat=True).distinct()
            response_data = {
                'contact': {
                    'primaryContactId': primary_contact.first().id,
                    'emails': [primary_contact.first().email] + list(distinct_emails),
                    'phoneNumbers': [primary_contact.first().phoneNumber] + list(distinct_phone_numbers),
                    'secondaryContactIds': secondary_contact_ids
                }
            }

        

        else:
            # Create a new contact as primary
            new_contact = Contact.objects.create(email=email, phoneNumber=phoneNumber, linkPrecedence='primary')
            response_data = {
                'contact': {
                    'primaryContactId': new_contact.id,
                    'emails': [new_contact.email],
                    'phoneNumbers': [new_contact.phoneNumber],
                    'secondaryContactIds': []
                }
            }

        return Response(response_data)
