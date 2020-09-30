
dict_ro = {}
dict_en = {}

dict_ro['i18n_welcome_p1'] = 'Bine ați venit!'
dict_ro['i18n_welcome_p2'] = '"Știința cetățenească" în Tulcea'
dict_ro['i18n_welcome_p3'] = 'Apreciem cu toții mâncarea sănătoasă. Cu toții avem nevoie de apă curată și energie. Cu această aplicație puteți găsi informații despre alimente, apă și energie în Tulcea și prin încărcarea personală a informațiilor puteți ajuta cercetătorii să înțeleagă cum sunt conectate aceste câmpuri. Mai concret, puteți găsi și încărca informații despre:'
dict_ro['i18n_welcome_p4'] = 'producători locali de alimente din orașul Tulcea și împrejurimi'
dict_ro['i18n_welcome_p5'] = 'servicii de producție precum brutării,'
dict_ro['i18n_welcome_p6'] = 'preferințele consumatorului cu privire la de ex. originea produselor alimentare,'
dict_ro['i18n_welcome_p7'] = 'furnizori de apă,'
dict_ro['i18n_welcome_p8'] = 'consumul de energie al cetățenilor.'
dict_ro['i18n_welcome_p9'] = 'Pentru explicații mai detaliate despre modul de utilizare a aplicației, vă rugăm să verificați diferitele subiecte prezentate în navigarea din partea de sus a paginii.'
dict_ro['i18n_welcome_p10'] = 'Aplicația a fost dezvoltată în cooperare cu INCDDD Tulcea. În prezent, testăm prima versiune a aplicației. Împărtășiți-ne părerea dvs. despre aceasta făcând clic pe linkul de feedback din partea de jos a acestei pagini!'
dict_ro['i18n_welcome_p11'] = 'Explorează!'

dict_en['i18n_welcome_p1'] = 'Welcome!'
dict_en['i18n_welcome_p2'] = 'Citizen Science in Tulcea'
dict_en['i18n_welcome_p3'] = 'We all love food. We all need clean water and energy. With this application you can find information on food, water and energy in Tulcea and by uploading information yourself you can help reseachers to understand how these fields are connected. More concrete, you can find and upload information about:'
dict_en['i18n_welcome_p4'] = 'local food producers in and around Tulcea,'
dict_en['i18n_welcome_p5'] = 'production services like bakeries,'
dict_en['i18n_welcome_p6'] = 'consumer preferences regarding e.g. the origin of food products,'
dict_en['i18n_welcome_p7'] = 'water suppliers,'
dict_en['i18n_welcome_p8'] = 'energy usage of citizens.'
dict_en['i18n_welcome_p9'] = 'For more detailed explanation on how to use the application, please check the different topics presented in the navigation at the top of the page.'
dict_en['i18n_welcome_p10'] = 'The application was developed in cooperation with the Tulcea City. We are currently testing the first version of the application. Share with us your opinion about it by clicking on the feedback link at the bottom of this page!'
dict_en['i18n_welcome_p11'] = 'Explore!'


class Dictionary():

    def __init__(self):
        self.dictionary_ro = dict_ro
        self.dictionary_en = dict_en

    def get_dict(self, language):

        if language == 'ro':
            return self.dictionary_ro
        else:
            return self.dictionary_en
