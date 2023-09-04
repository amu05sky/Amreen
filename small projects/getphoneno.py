import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo=input("Enter Phone number with country code(+xx xxxxxxxxxx):")
mobileNo=phonenumbers.parse(mobileNo)+91 
if phonenumbers.is_valid_number(mobileNo):
    print('Phone Number belongs to region :',timezone.time_zones_for_number(mobileNo))
    print('Service Provider : ',carrier.name_for_number(mobileNo,"en"))
    print('Phone number belongs to country : ',geocoder.description_for_number(mobileNo,"en"))
else:
    print("Please enter valid mobile number")