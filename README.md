# A project for the E-Commerce course, 2018 Spring.

## Introduction

This project is based on [saleor](https://github.com/mirumee/saleor), an e-commerce storefront for Python and Django. This project focuses on resolving some problems of the deom of saleor. For example, we plan to fix the placement problem of the search bar and add a comment bar for better presenting the information of a product. 

## Hands-Up Steps

1.Install saleor by following the [INSTALL.txt](./INSTALL.txt).

2.Replace the folder "saleor/" with our new folder "e-commerce/saleor"

e.g., we download our project under the saleor/ directory:

```
cd saleor/
mv saleor/ saleor_bak/
git clone https://github.com/Wasdns/e-commerce.git
mv e-commerce/saleor/ ./
```

3.Start local server:

```
SECRET_KEY='saleor' python manage.py runserver
```

Then you can visit `localhost:8000`.

## Author

Chenyao Liu @thousfeet and Xiang Chen @Wasdns.
