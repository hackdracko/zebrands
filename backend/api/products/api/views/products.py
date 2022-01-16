from rest_framework.viewsets import ModelViewSet
from core.pagination import CustomPagination
from products.models import *
from users.models import *
from products.api.serializers import *
from api.permissions import IsAdminOrAnonymous
from django.http import HttpResponse, JsonResponse
from rest_framework import status
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ProductsModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrAnonymous]
    pagination_class = CustomPagination
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def update(self, request, pk=None):
        try:
            product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return HttpResponse(status=404)

        serializer = ProductsSerializer(product, data=request.data) 
        if serializer.is_valid(): 
            serializer.save()
            admins = User.objects.filter(is_staff=1)
            for admin in admins:
                if admin.email:
                    mail_content = 'The product ' + pk + ' was updated.'
                    #The mail addresses and password
                    sender_address = 'patolin00755@gmail.com'
                    sender_pass = 'amohyrkaujkfajte'
                    receiver_address = admin.email
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = 'Zebrands notification product updated'   #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # http_method_names = ['get']