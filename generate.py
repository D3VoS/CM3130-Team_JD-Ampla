
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ampla.settings')

import django
django.setup()


from Store.models import Product
from Core.models import Contact
from Accounts.models import User

def generateUser():
    if len(User.objects.filter(email="testing@ampla.com")) == 0:

        new_user = User.objects.create(email="testing@ampla.com", first_name="John", last_name="Doe", password="test")
        new_user.save()
        print("User Created")
        return new_user
    else:
        return User.objects.filter(email="testing@ampla.com")[0]

def generateProduct(name, price, imageLink, productLink):
    if len(Product.objects.filter(productName=name)) == 0:
        product = Product(productName=name,productPrice=price,productImageLink=imageLink,productLink=productLink)
        product.save()
        print(f"Created object: {name} with price of {price}")
    else:
        print(f"object with name {name} already exists: Skipping")

def generateContacts(user, title, message):
    if len(Contact.objects.filter(title=title)) == 0:
        contact = Contact(creator=user, title=title, message=message)
        contact.save()
        print("Contact Form Created")
    else:
        print("Contact Form already exists")
        


def run():
    generateProduct("Women's Powerskin Carbon-Glide Closed Back – FINA approved", 410.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/003664730_001_3.jpg", "https://www.arenawaterinstinct.com/en_uk/003664-women-s-powerskin-carbon-glide-closed-back-fina-approved.html")
    generateProduct("Teens and Women's arena Reusable Face Mask Carbon", 8.90, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/004722750_001.jpg", "https://www.arenawaterinstinct.com/en_uk/004722-teens-and-women-s-arena-reusable-face-mask-carbon.html")
    generateProduct("Women's Powerskin Carbon-DUO Bottom – FINA approved", 190.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/002758725_001_11.jpg", "https://www.arenawaterinstinct.com/en_uk/002758-women-s-powerskin-carbon-duo-bottom.html")
    generateProduct("Cobra Ultra Goggles", 36.00 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/1/E/1E03390_001.jpg" ,"https://www.arenawaterinstinct.com/en_uk/cobra-ultra.html")
    generateProduct("3D Soft Cap", 35.00 ," https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/000400501_001.jpg", "https://www.arenawaterinstinct.com/en_uk/000400-3d-soft-cap.html")
    generateProduct("Gym Soft Towel" , 20.00 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/001994810_001.jpg ", "https://www.arenawaterinstinct.com/en_uk/001994-gym-soft-towel.html")
    generateProduct("Team Backpack 45", 60.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/002436600_001.jpg", "https://www.arenawaterinstinct.com/en_uk/002436-team-backpack-45.html")
    generateProduct("Goggles Case", 9.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/1/e/1e048507_001.jpg", "https://www.arenawaterinstinct.com/en_uk/goggle-case.html")
    generateProduct("Team Mesh", 11.25, " https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/002495900_001.jpg", " https://www.arenawaterinstinct.com/en_uk/002495-team-mesh.html")
    generateProduct("Women's Powerskin ST 2.0 Open Back Limited Edition – FINA approved" , 85.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/000812703_001_1.jpg", "https://www.arenawaterinstinct.com/en_uk/000812-women-s-powerskin-st-2-0-full-body-limited-edition.html")
    generateProduct("Women's Powerskin Carbon-Ultra Open Back – FINA approved" , 322.00 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/2/A/2A31285_001.jpg" , "https://www.arenawaterinstinct.com/en_uk/c852a312-women-s-powerskin-carbon-ultra-full-body-short-leg-open-back.html")
    generateProduct("Women's POWERSKIN Carbon-Air Closed back – FINA approved" , 220.00 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/1/a/1a645913_001_3.jpg", "https://www.arenawaterinstinct.com/en_uk/1a645-women-s-powerskin-carbon-air-closed-back.html")
    generateProduct("Women's Powerskin R-EVO ONE Open Back – FINA approved" , 142.50 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/001438143_001_18.jpg" , "https://www.arenawaterinstinct.com/en_uk/001438-women-s-powerskin-r-evo-one-full-body-short-leg-open-back.html")


    user = generateUser()

    generateContacts(user, "Hi", "Hello")
    generateContacts(user, "Hello", "Hi")
    generateContacts(user, "Hello, I have an issue", "yes")
    generateContacts(user, "Goodmorning, I have an issue", "yes")
    generateContacts(user, "Getting a bit old now, I have an issue", "yes")
    generateContacts(user, "Cannae buy fit am wantin, I have an issue", "yes")
    generateContacts(user, "yer sites no workin, I have an issue", "yes")
    generateContacts(user, "am leavin, I have an issue", "yes")

if __name__ == "__main__":
    run()