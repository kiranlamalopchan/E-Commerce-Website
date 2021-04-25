from django.views import View
from django.shortcuts import render
from store.models import Banner, Payment, Section, Brand, Product, Mac, Ipad, IPhone, Beatsbydre, Applecare, \
    Appleaccessories, Bose, Logo


class Homeview(View):
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
        banners = Banner.get_all_banners()
        sections = Section.get_section_detail()
        brands = Brand.get_all_brands()
        products = Product.get_all_products()
        payments = Payment.get_all_payment()
        logo = Logo.get_logo()

        context = {'macs': macs, 'ipads': ipads, 'banners': banners, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose, 'sections': sections,
                   'brands': brands, 'products': products, 'payments': payments, 'logo': logo}
        return render(request, 'home.html', context)
