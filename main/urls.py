from django.urls import path
from main import views



urlpatterns = [
    path('',views.login_view , name='login'),
    path('register/', views.register_view, name='register'),
    path('main/', views.main, name='main'),
    path('equipment/', views.equipment, name='equipment'),
    path('tailored_recommendations/', views.recommendations, name='tailored_recommendations'),
    path('prediction/', views.prediction, name='prediction'),
    path('contact/', views.contact_view, name='contact'),
    path('page1/', views.page1, name='pageone'),
    path('page2/', views.page2, name='pagetwo'),
    path('page3/', views.page3, name='pagethree'),
    path('page4/', views.page4, name='pagefour'),
    path('page5/', views.page5, name='pagefive'),
    path('page7/', views.page6, name='pagesix'),
    path('page8/', views.page7, name='pageseven'),
    path('page9/', views.page8,name='pagenine'),
    path('page10/', views.page9,name='pageten'),
    path('faq/', views.faq, name='faq'),
    path('results/', views.results, name='results'),
    path('Quatation1/', views.Quotation1, name='Quotation1'),
    path('Quatation2/', views.Quotation2, name='Quotation2'),
    path('Quatation3/', views.Quotation3, name='Quotation3'),
    path('consultation/', views.consultation, name='consultation'),
    path('ref1/', views.design, name='ref1'),
    path('ref2/', views.installation, name='ref2'),
    path('ref3/', views.maintenance, name='ref3'),
    path('ref4/', views.ref4, name='ref4'),
    path('model/', views.model, name='model'),

    
    


    
    

    
]    