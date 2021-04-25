from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.customers import Customer
from django.contrib.auth.hashers import check_password
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose, Payment


class Login(View):
    return_url = None
    def get(self, request):
        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        payments = Payment.get_all_payment()
        bose = Bose.get_all_boselist()
        # -------- Nav link List End------
        Login.return_url = request.GET.get('return_url')

        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose':bose, 'payments': payments
        }
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        ob_customer = Customer.get_customer_forlogin(username)
        values = {'username': username}
        # Following code matches object not character of object
        if ob_customer:
            flag = check_password(password, ob_customer.password)
            if flag:
                request.session['userid'] = ob_customer.id
                request.session['username'] = ob_customer.username

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('home')
            else:
                errmsg = "Username and Password didn't match."
        else:
            errmsg = "Username and Password didn't match."

        context = {'errmsg': errmsg, 'values': values}
        return render(request, 'login.html', context)


