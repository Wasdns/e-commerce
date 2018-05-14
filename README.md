# A project for the E-Commerce course, 2018 Spring.

## Introduction

This project is based on [saleor](https://github.com/mirumee/saleor), an e-commerce storefront for Python and Django. This project focuses on resolving some problems of the deom of saleor. For example, we plan to fix the placement problem of the search bar and add a comment bar for better presenting the information of a product. 

## Hands-Up Steps

1.Install saleor by following the [INSTALL.txt](./INSTALL.txt).

2.Start local server:

```
SECRET_KEY='saleor' python manage.py runserver
```

Then you can visit `localhost:8000`.

3.Login as a superuser:

You can use the account "saleor@mail.com" with the password "saleor" to login into the saleor dashboard as a superuser.

4.Add some products to your e-commerce website:

Go to the dashboard, and create the following things in order:
- Collections: add the label of your goods;
- Categories: add the category of your goods;
- Products: add your goods to a specific category.

We provide some available figures of goods for eatting under the folder [goods/figures](goods/figures). You can exploit these figures as the figures of your goods.

## Author

Chenyao Liu @thousfeet and Xiang Chen @Wasdns.
