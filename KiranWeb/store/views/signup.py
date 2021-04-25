from django.shortcuts import render, redirect
from store.models.customers import Customer
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models import Payment
from store.models import Ipad, IPhone, Applecare, Appleaccessories, Bose, Beatsbydre, Mac


class Signup(View):
    def validates(self, customer):
        errmsg = None
        if not customer.username:
            errmsg = "Username must be enter !!"
        elif len(customer.username) < 4:
            errmsg = "Username must be be more than 4 Character"
        elif len(customer.username) > 25:
            errmsg = "Username must be be less than 25 Character"
        elif not customer.email:
            errmsg = "Must filled email"
        elif not customer.mobilenumber:
            errmsg = "Mobile Number Must be Filled."
        elif len(customer.mobilenumber) < 10:
            errmsg = "Mobile Number must be 10 Character"
        elif len(customer.mobilenumber) > 10:
            errmsg = "Mobile Number must be 10 character second"
        elif customer.check != "checked":
            errmsg = "Must Check Terms and Conditions"
        elif customer.usernamevalidation():
            errmsg = "Username Already Exists. Try Another!"
        return errmsg

    @staticmethod
    def get(request):
        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        bose = Bose.get_all_boselist()
        # -------- Nav link List End------

        payments = Payment.get_all_payment()
        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                   'payments': payments, }
        return render(request, 'signup.html', context)

    def post(self, request):
        postdata = request.POST
        username = postdata.get('uname')
        password = postdata.get('upass')
        email = postdata.get('uemail')
        mobilenumber = postdata.get('umobile')
        address = postdata.get('uaddress')
        city = postdata.get('ucity')
        country = postdata.get('ucountry')
        zip = postdata.get('uzip')
        check = postdata.get('ucheck')

        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        bose = Bose.get_all_boselist()
        payments = Payment.get_all_payment()
        # -------- Nav link List End------

        ob_customer = Customer(username=username, password=password, email=email, mobilenumber=mobilenumber,
                               address=address, city=city, country=country, zip=zip, check=check)

        err_message = self.validates(ob_customer)
        if not err_message:
            ob_customer.password = make_password(ob_customer.password)
            ob_customer.signupcustomer()
            return redirect('home')
        else:
            # if error occur
            errorvalue = {'username': username, 'mobilenumber': mobilenumber, 'email': email, 'address': address,
                          'city': city, 'country': country, 'zip': zip}
            context = {'errmsg': err_message, 'values': errorvalue, 'macs': macs, 'ipads': ipads, 'iphones': iphones,
                       'beats': beats, 'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                       'payments': payments, }
        return render(request, 'signup.html', context)
