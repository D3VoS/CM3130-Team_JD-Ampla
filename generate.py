
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ampla.settings')

import django
django.setup()


from Store.models import Product


def generateProduct(name, price, imageLink, productLink):
    if len(Product.objects.filter(productName=name)) == 0:
        product = Product(productName=name,productPrice=price,productImageLink=imageLink,productLink=productLink)
        product.save()
        print(f"Created object: {name} with price of {price}")
    else:
        print(f"object with name {name} already exists: Skipping")
def run():
    generateProduct("Women's Powerskin Carbon-Glide Closed Back – FINA approved", 410.00, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/003664730_001_3.jpg", "https://www.arenawaterinstinct.com/en_uk/003664-women-s-powerskin-carbon-glide-closed-back-fina-approved.html%22")
    generateProduct("Teens and Womens arena Reusable Face Mask Carbon", 8.90, "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/004722750_001.jpg", "https://www.arenawaterinstinct.com/en_uk/004722-teens-and-women-s-arena-reusable-face-mask-carbon.html")
    generateProduct("Cobra Ultra Goggles", 36.00 , "https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/1/E/1E03390_001.jpg" ,"https://www.arenawaterinstinct.com/en_uk/cobra-ultra.html")
    generateProduct("3D Soft Cap", 35.00 ," https://static.arenawaterinstinct.com/media/catalog/product/cache/8/image/2000x/040ec09b1e35df139433887a97daa66f/0/0/000400501_001.jpg", "https://www.arenawaterinstinct.com/en_uk/000400-3d-soft-cap.html")



if __name__ == "__main__":
    run()