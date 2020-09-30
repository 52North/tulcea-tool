define(['wq/store', 'wq/router'], function (ds, router) { 'use strict';

// from https://stackoverflow.com/questions/5639346/what-is-the-shortest-function-for-reading-a-cookie-by-name-in-javascript
function getCookieValue(a) {
    var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
    return b ? b.pop() : '';
}

var dict = {
  'en': {
    'i18n_welcome_p1':'Welcome!',
    'i18n_welcome_p2': 'Citizen Science in Tulcea',
    'i18n_welcome_p3': 'We all love food. We all need clean water and energy. With this application you can find information on food, water and energy in Tulcea and by uploading information yourself you can help reseachers to understand how these fields are connected. More concrete, you can find and upload information about:',
    'i18n_welcome_p4': 'local food producers in and around Tulcea,',
    'i18n_welcome_p5': 'production services like bakeries,',
    'i18n_welcome_p6': 'consumer preferences regarding e.g. the origin of food products,',
    'i18n_welcome_p7': 'water suppliers,',
    'i18n_welcome_p8': 'energy usage of citizens.',
    'i18n_welcome_p9': 'For more detailed explanation on how to use the application, please check the different topics presented in the navigation at the top of the page.',
    'i18n_welcome_p10': 'The application was developed in cooperation with the Tulcea City. We are currently testing the first version of the application. Share with us your opinion about it by clicking on the feedback link at the bottom of this page!',
    'i18n_welcome_p11': 'Explore!',
    'i18n_about_p1': 'About',
    'i18n_about_p2': 'The EU funded project "Creating Interfaces" has the goal to build capacity for integrated governance at the Food-Water-Energy-nexus in cities on the water. The city of Tulcea is participating as a case study site. On this website, citizens in and around Tulcea can help understanding the connection between food, water and energy by submitting data about these three topics. ',
    'i18n_about_p3': 'Moreover, citizens can find information about these complexes which might help in their daily decisions, e.g. where to buy healthy and local food. If you need assistance in using the website, have a look at the different topics in the navigation bar at the top of the page. Of course, you can also contact the project team via <a href="mailto:iulian.nichersu@ddni.ro">iulian.nichersu@ddni.ro</a>',
    'i18n_about_p4': 'More complex visualizations and analyses can be found here (add link). There is also a story map (add link).',
    'i18n_food_p1': 'Food',
    'i18n_food_p2': 'On this site, you can find and submit information about food in and around Tulcea.',
    'i18n_food_p3': 'You can add food producers and production services with their sale points and storage points.',
    'i18n_food_p4': 'Add sale point',
    'i18n_food_p5': 'List of sale points',
    'i18n_food_p6': 'Add storage point',
    'i18n_food_p7': 'List of storage points',
    'i18n_food_p8': 'Add producer',
    'i18n_food_p9': 'List of producers',
    'i18n_food_p10': 'Add production service',
    'i18n_food_p11': 'List of production services',
    'i18n_food_p12': 'Add consumer',
    'i18n_food_p13': 'List of consumers',
  },
  'ro': {
    'i18n_welcome_p1': 'Bine ați venit!',
    'i18n_welcome_p2': '"Știința cetățenească" în Tulcea',
    'i18n_welcome_p3': 'Apreciem cu toții mâncarea sănătoasă. Cu toții avem nevoie de apă curată și energie. Cu această aplicație puteți găsi informații despre alimente, apă și energie în Tulcea și prin încărcarea personală a informațiilor puteți ajuta cercetătorii să înțeleagă cum sunt conectate aceste câmpuri. Mai concret, puteți găsi și încărca informații despre:',
    'i18n_welcome_p4': 'producători locali de alimente din orașul Tulcea și împrejurimi',
    'i18n_welcome_p5': 'servicii de producție precum brutării,',
    'i18n_welcome_p6': 'preferințele consumatorului cu privire la de ex. originea produselor alimentare,',
    'i18n_welcome_p7': 'furnizori de apă,',
    'i18n_welcome_p8': 'consumul de energie al cetățenilor.',
    'i18n_welcome_p9': 'Pentru explicații mai detaliate despre modul de utilizare a aplicației, vă rugăm să verificați diferitele subiecte prezentate în navigarea din partea de sus a paginii.',
    'i18n_welcome_p10': 'Aplicația a fost dezvoltată în cooperare cu INCDDD Tulcea. În prezent, testăm prima versiune a aplicației. Împărtășiți-ne părerea dvs. despre aceasta făcând clic pe linkul de feedback din partea de jos a acestei pagini!',
    'i18n_welcome_p11': 'Explorează!',
    'i18n_about_p1': 'Despre',
    'i18n_about_p2': 'Proiectul finanțat de UE „Crearea de interfețe” are scopul de a dezvolta capacități pentru o guvernanță integrată a legăturii Alimentație-Apă-Energie din orașele riverane. Orașul Tulcea a fost ales ca studiu de caz. Pe acest site web, cetățenii din orașul Tulcea si imprejurimi pot ajuta la înțelegerea legăturii dintre alimente, apă și energie prin transmiterea datelor despre aceste trei subiecte.',
    'i18n_about_p3': 'Mai mult, cetățenii pot găsi informații despre aceste complexe care ar putea ajuta în deciziile lor zilnice, de ex. de unde să cumpere mâncare sănătoasă și locală. Dacă aveți nevoie de asistență în utilizarea site-ului web, aruncați o privire asupra diferitelor subiecte din bara de navigare din partea de sus a paginii. Desigur, puteți contacta și echipa de proiect pe adresa de email: <a href="mailto:iulian.nichersu@ddni.ro">iulian.nichersu@ddni.ro</a>',
    'i18n_about_p4': 'Vizualizări și analize mai complexe pot fi găsite aici (adăugați link). Există, de asemenea, o hartă a poveștii fiecarui oras studiu de caz din cadrul proiectului(adăugați link).',
    'i18n_food_p1': 'Alimentație',
    'i18n_food_p2': 'Pe acest site, puteți găsi și trimite informații despre mâncarea din Tulcea și împrejurimi.',
    'i18n_food_p3': 'Puteți adăuga producători de produse alimentare și servicii de producție cu punctele lor de vanzare și de depozitare.',
    'i18n_food_p4': 'Adaugă punct de vanzare',
    'i18n_food_p5': 'Lista punctelor de vânzare',
    'i18n_food_p6': 'Adaugă punct de depozitare',
    'i18n_food_p7': 'Listă puncte de depozitare',
    'i18n_food_p8': 'Adaugă producător',
    'i18n_food_p9': 'Lista producătorilor',
    'i18n_food_p10': 'Adaugă servicii de producție',
    'i18n_food_p11': 'Lista serviciilor de producție',
    'i18n_food_p12': 'Adaugă consumator',
    'i18n_food_p13': 'Lista consumatorilor',
  }
};







var i18n = {
    name: 'i18n'
};

var $;

i18n.init = function (config) {
    $ = config && config.jQuery || window.jQuery;

    this.dict = dict;

    // Set language
    var lang = getCookieValue('django_language');  // cookie language preference

    if (!lang) {
      if (navigator.language == 'en' || navigator.language == 'ro') {
        this.language = navigator.language;       // browser language preference
      } else {
        this.language = 'ro';                     // fall-back language, should be equal to LANGUAGE_CODE in base.py for consistency
      }
    } else {
      this.language = lang;
    }

    // Set language in select menu
    $('select[class="language"]').val(this.language).change();

    // Use cookie also here?
    ds.set('wq-language', this.language);

};


i18n.context = function(context, routeInfo) {
    return this.dict[this.language];
};


i18n.run = function ($page, routeInfo) {

  var parent = this;

  $page.on('change', 'select[class="language"]', function(evt) {

    // Set language taken from widget
    parent.language = $(evt.target).val();

    // Set cookie to be used by django.middleware.locale.LocaleMiddleware
    document.cookie = "django_language=".concat(parent.language).concat(";SameSite=Lax") ;

    // Reload page once
    // Use cookie also here?
    ds.get('wq-language').then(function(language) {

      if( language != parent.language ) {
        ds.set('wq-language', parent.language);
        window.location.reload();
      }

    });

  });

  $page.ready( function() {
    $('select[class="language"]').val(parent.language).change();
  });


};

return i18n;

});
