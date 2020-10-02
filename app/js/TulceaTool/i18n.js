define(['wq/store', 'wq/router'], function (ds, router) { 'use strict';

// from https://stackoverflow.com/questions/5639346/what-is-the-shortest-function-for-reading-a-cookie-by-name-in-javascript
function getCookieValue(a) {
    var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
    return b ? b.pop() : '';
}

var dict = {
  'en': {
    'i18n_welcome_p1': 'Welcome!',
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
    'i18n_auth_message': 'Currently, this website is only open for authenticated users. Please insert your username and password to proceed.',
    'i18n_username': 'Username',
    'i18n_password': 'Password',
    'i18n_explore_tool': 'Explore the tool!',
    'i18n_about_p1': 'About',
    'i18n_about_p2': 'The EU funded project "Creating Interfaces" has the goal to build capacity for integrated governance at the Food-Water-Energy-nexus in cities on the water. The city of Tulcea is participating as a case study site. On this website, citizens in and around Tulcea can help understanding the connection between food, water and energy by submitting data about these three topics. ',
    'i18n_about_p3': 'Moreover, citizens can find information about these complexes which might help in their daily decisions, e.g. where to buy healthy and local food. If you need assistance in using the website, have a look at the different topics in the navigation bar at the top of the page. Of course, you can also contact the project team via <a href="mailto:iulian.nichersu@ddni.ro">iulian.nichersu@ddni.ro</a>',
    'i18n_about_p4': 'More complex visualizations and analyses can be found here (add link). There is also a story map (add link).',
    'i18n_food_p1': 'Food',
    'i18n_food_p2': 'On this site, you can find and submit information about food in and around Tulcea.',
    'i18n_food_p3': 'You can add food producers and production services with their sale points and storage points.',
    'i18n_water_p1': 'Water',
    'i18n_water_p2': 'On this site, you can find and submit information about water suppliers in and around Tulcea.',
    'i18n_energy_p1': 'Energy',
    'i18n_energy_p2': 'On this site, you can submit information about your usage of energy.',
    'i18n_home': 'Home',
    'i18n_add': 'Add',
    'i18n_edit': 'Edit',
    'i18n_submit': 'Submit',
    'i18n_add_sale_point': 'Add sale point',
    'i18n_sale_point_list': 'List of sale points',
    'i18n_sale_point': 'Sale point',
    'i18n_show_sale_points': 'Show sale points',
    'i18n_this_sale_point': 'This sale point',
    'i18n_all_sale_points': 'All sale points',
    'i18n_add_storage_point': 'Add storage point',
    'i18n_storage_point_list': 'List of storage points',
    'i18n_storage_point': 'Storage point',
    'i18n_show_storage_points': 'Show storage points',
    'i18n_this_storage_point': 'This storage point',
    'i18n_all_storage_points': 'All storage points',
    'i18n_add_producer': 'Add producer',
    'i18n_producer_list': 'List of producers',
    'i18n_show_producers': 'Show producers',
    'i18n_this_producer': 'This producer',
    'i18n_all_producers': 'All producers',
    'i18n_producer': 'producer',
    'i18n_add_production_service': 'Add production service',
    'i18n_production_service_list': 'List of production services',
    'i18n_show_production_services': 'Show production services',
    'i18n_this_production_service': 'This production service',
    'i18n_all_production_services': 'All production services',
    'i18n_production_service': 'production service',
    'i18n_add_consumer': 'Add consumer',
    'i18n_consumer_list': 'List of consumers',
    'i18n_show_consumers': 'Show consumers',
    'i18n_consumer': 'consumer',
    'i18n_add_watersupplier': 'Add water supplier',
    'i18n_watersupplier_list': 'List of water suppliers',
    'i18n_show_watersuppliers': 'Show water suppliers',
    'i18n_this_watersupplier': 'This water supplier',
    'i18n_all_watersuppliers': 'All water suppliers',
    'i18n_watersupplier': 'water supplier',
    'i18n_add_energyusage': 'Add energy usage',
    'i18n_energyusage_list': 'List of energyusages',
    'i18n_show_energyusages': 'Show energy usages',
    'i18n_this_energyusage': 'This energy usage',
    'i18n_all_energyusages': 'All energy usages',
    'i18n_energyusage': 'energy usage',
    'i18n_this_energy_usage': 'This energy usage',
    'i18n_add_feedback': 'Add feedback',
    'i18n_feedback_list': 'List of feedbacks',
    'i18n_show_feedbacks': 'Show feedbacks',
    'i18n_feedback': 'feedback',
    'i18n_general': 'General',
    'i18n_name': 'Name',
    'i18n_type': 'Type',
    'i18n_type_choices': [{'name': "certificate", 'label': "Certificate of producer"}, {'name': "small_company", 'label': "Small company"}, {'name': "small_gardening", 'label': "Small gardening"}],
    'i18n_products': 'Main product(s)',
    'i18n_contact': 'Contact',
    'i18n_address': 'Address',
    'i18n_telephone': 'Telephone',
    'i18n_email': 'E-mail',
    'i18n_website': 'Website',
    'i18n_location': 'Location',
    'i18n_location_mode': 'Location Mode',
    'i18n_toggle_choices': [{'name': "gps", 'label': "Use GPS"}, {'name': "interactive",'label': "Point on Map"}, {'name': "manual", 'label': "Enter Manually"}],
    'i18n_latitude': 'Latitude',
    'i18n_longitude': 'Longitude',
    'i18n_accuracy': 'GPS Accuracy',
    'i18n_yes': 'Yes',
    'i18n_no': 'No',
    'i18n_water_energy': 'Water and energy',
    'i18n_irrigation_use': 'Do you use water for irrigation?',
    'i18n_irrigation_use_choices': [{'name': "yes", 'label': "Yes"}, {'name': "no",'label': "No"}],
    'i18n_water_quantity': 'Water quantity (in m³ per year)',
    'i18n_water_quality': 'Water quality',
    'i18n_irrigation_quality_choices': [{'name': "source", 'label': "From source"}, {'name': "underground",'label': "Underground water"}],
    'i18n_irrigation_interest': 'Do you have interest to use water for irrigation?',
    'i18n_irrigation_interest_choices': [{'name': "yes", 'label': "Yes"}, {'name': "no",'label': "No"}],
    'i18n_electrical_consumption': 'Average electrical consumption (in kWh per year)',
    'i18n_distance': 'Distance: producer → storage → sale point (km)',
    'i18n_distance_hint': 'To calculate the distance you can use the line tool in the map above. Be careful when the location mode "Point on Map" is selected. In this case, when drawing a line the location of the producer will be changed. To avoid this, you can temporarily choose "Enter Manually" as location mode.',
    'i18n_production': 'Production (in kg/ha per year)',
    'i18n_surface': 'Surface (in ha)',
    'i18n_uses': 'Uses',
    'i18n_use_choices': [{'name': "homefood", 'label': "Homefood"}, {'name': "other",'label': "Other"}],
    'i18n_fertilizer_use': 'Use of fertilizer',
    'i18n_fertilizer_choices': [{'name': "natural", 'label': "Natural"}, {'name': "artificial",'label': "Artificial"}],
    'i18n_products_info': 'Products related information',
    'i18n_source_raw_material': 'Source of raw material',
    'i18n_water_quantity_month': 'Water quantity need (in m³ per month)',
    'i18n_energy_consumption': 'Average energy consumption (in kWh per month)',
    'i18n_distance2': 'Distance: production site → storage → sale point (km)',
    'i18n_distance_hint2': 'To calculate the distance you can use the line tool in the map above. Be careful when the location mode "Point on Map" is selected. In this case, when drawing a line the location of the production service will be changed. To avoid this, you can temporarily choose "Enter Manually" as location mode.',
    'i18n_covid_measures': 'Are the measures taken in the context of limiting COVID-19 infection affecting you?',
    'i18n_covid_affected_choices': [{'name': "yes", 'label': "Yes"}, {'name': "no",'label': "No"}],
    'i18n_effects': 'The main effect is',
    'i18n_main_effect_choices': [{'name': "scaderea_vanzarilor", 'label': "Scăderea vânzărilor"}, {'name': "scaderea_cifrei",'label': "Scăderea cifrei de afaceri"}, {'name': "disponibilizari",'label': "Disponibilizări"}, {'name': "intarzieri",'label': "Întârzieri la plata furnizorilor"}, {'name': "dificultati",'label': "Dificultăţi la încasare"}, {'name': "restrangerea",'label': "Restrângerea activității"}, {'name': "suspendarea",'label': "Suspendarea temporară a activităţii"}, {'name': "inchiderea",'label': "Închiderea firmei"}, {'name': "reprofilare",'label': "Reprofilare"}],
    'i18n_turnover_decrease': 'What is the percentage by which you estimate the decrease in turnover?',
    'i18n_gender': 'Gender',
    'i18n_gender_choices': [{'name': "male", 'label': "Male"}, {'name': "female",'label': "Female"}],
    'i18n_age': 'Age',
    'i18n_income': 'Income (Euro)',
    'i18n_income_choices': [{'name': "less_1500", 'label': "< 1500 / family member"}, {'name': "more_1500",'label': "> 1500 / family member"}, {'name': "na",'label': "No answer"}],
    'i18n_consumer_profile': 'Consumer profile',
    'i18n_source_raw_aliments': 'Source of the raw aliments for food (number selection - times per week)',
    'i18n_big_store': 'Big store chains',
    'i18n_big_chain_store_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "ca. 3"}, {'name': "more",'label': "More"}],
    'i18n_local_store': 'Local chain stores',
    'i18n_local_chain_store_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "ca. 3"}, {'name': "more",'label': "More"}],
    'i18n_small_shop': 'Small shops',
    'i18n_small_shop_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "ca. 3"}, {'name': "more",'label': "More"}],
    'i18n_market': 'Market',
    'i18n_market_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "ca. 3"}, {'name': "more",'label': "More"}],
    'i18n_main_transport': 'Main transport',
    'i18n_transport_choices': [{'name': "car", 'label': "Personal car"}, {'name': "public",'label': "Public transport"}, {'name': "bike",'label': "By bike"}, {'name': "foot",'label': "By foot"}],
    'i18n_bio_use': 'Bio products use',
    'i18n_bio_choices': [{'name': "frequently", 'label': "Frequently"}, {'name': "sometimes",'label': "Sometimes"}, {'name': "no_use",'label': "No use"}],
    'i18n_product_origin': 'Local/national products use',
    'i18n_local_choices': [{'name': "frequently", 'label': "Frequently"}, {'name': "sometimes",'label': "Sometimes"}, {'name': "no_use",'label': "No use"}],
    'i18n_tap_water': 'Quantity of consumed tap water (in m³)',
    'i18n_bottled_water': 'Quantity of consumed bottled water (in m³)',
    'i18n_waste_water': 'Waste water',
    'i18n_waste_water_choices': [{'name': "sewage", 'label': "Sewage system"}, {'name': "septic", 'label': "Septic tanks"}, {'name': "no_treatment",'label': "No treatment at all"}],
    'i18n_food_priorization': 'Priorization in food choice',
    'i18n_priorization_choices': [{'name': "price", 'label': "Price"}, {'name': "ecological_impact",'label': "Ecological impact"}, {'name': "aquisition_time",'label': "Time for acquisition"}, {'name': "health_impact",'label': "Health impact"}],
    'i18n_location_headquarters': 'Location of headquarters',
    'i18n_water_supply': 'Water supply',
    'i18n_bogza': 'Bogza (in m³)',
    'i18n_mila': 'Mila (in m³)',
    'i18n_irrigation_supply': 'Irrigation supply',
    'i18n_irrigation_supply_choices': [{'name': "source", 'label': "From source"}, {'name': "underground",'label': "Underground water"}],
    'i18n_energy_type': 'What type of energy do you use?',
    'i18n_energy_type_choices': [{'name': "national", 'label': "National system"}, {'name': "renewable",'label': "Renewable"}, {'name': "both", 'label': "Both"}],
    'i18n_more_renewable': 'Would you like to use more renewable energy?',
    'i18n_more_renewable_choices': [{'name': "yes", 'label': "Yes"}, {'name': "no",'label': "No"}],
    'i18n_type_renewable': 'What type of renewable energy do you use?',
    'i18n_renewable_type_choices': [{'name': "solar", 'label': "Solar"}, {'name': "wind",'label': "Wind"}, {'name': "water", 'label': "Water"}, {'name': "geothermal", 'label': "Geothermal"}, {'name': "bio", 'label': "Bio"}, {'name': "other", 'label': "Other"}],
    'i18n_renewable_hint': 'Please add the location of the renewable energy source that you use. <br> <br> You can choose between three options for setting the location. In the first option, the location is taken from the gps of your device (if available). As second option, you can click on the map below, and as third option you can insert the latitude and longitude directly in the fields below. The last option is only recommended for experienced users.',
    'i18n_useful': 'The application is useful',
    'i18n_usability_choices': [{'name': "strong_agree", 'label': "I strongly agree"}, {'name': "rather_agree",'label': "I&#x27;d rather agree"}, {'name': "undecided",'label': "Neither disagree nor agree"}, {'name': "rather_disagree",'label': "I&#x27;d rather disagree"}, {'name': "strong_disagree",'label': "I strongly disagree"}],
    'i18n_attractive': 'The application is visually (graphically) attractive',
    'i18n_attractiveness_choices': [{'name': "strong_agree", 'label': "I strongly agree"}, {'name': "rather_agree",'label': "I&#x27;d rather agree"}, {'name': "undecided",'label': "Neither disagree nor agree"}, {'name': "rather_disagree",'label': "I&#x27;d rather disagree"}, {'name': "strong_disagree",'label': "I strongly disagree"}],
    'i18n_maps_helpful': 'Maps help to use the application',
    'i18n_maps_choices': [{'name': "strong_agree", 'label': "I strongly agree"}, {'name': "rather_agree",'label': "I&#x27;d rather agree"}, {'name': "undecided",'label': "Neither disagree nor agree"}, {'name': "rather_disagree",'label': "I&#x27;d rather disagree"}, {'name': "strong_disagree",'label': "I strongly disagree"}],
    'i18n_clear_instruction': 'Instruction on how to use the application is easy to understand',
    'i18n_clarity_choices': [{'name': "strong_agree", 'label': "I strongly agree"}, {'name': "rather_agree",'label': "I&#x27;d rather agree"}, {'name': "undecided",'label': "Neither disagree nor agree"}, {'name': "rather_disagree",'label': "I&#x27;d rather disagree"}, {'name': "strong_disagree",'label': "I strongly disagree"}],
    'i18n_main_attraction': 'What was the main attraction?',
    'i18n_additional_functions': 'What other functions should the application have?',
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
    'i18n_auth_message': 'În prezent, acest site web este deschis doar pentru utilizatorii autentificați. Vă rugăm să introduceți numele de utilizator și parola pentru a continua.',
    'i18n_username': 'Nume de utilizator',
    'i18n_password': 'Parola',
    'i18n_explore_tool': 'Explorați aplicația!',
    'i18n_about_p1': 'Despre',
    'i18n_about_p2': 'Proiectul finanțat de UE „Crearea de interfețe” are scopul de a dezvolta capacități pentru o guvernanță integrată a legăturii Alimentație-Apă-Energie din orașele riverane. Orașul Tulcea a fost ales ca studiu de caz. Pe acest site web, cetățenii din orașul Tulcea si imprejurimi pot ajuta la înțelegerea legăturii dintre alimente, apă și energie prin transmiterea datelor despre aceste trei subiecte.',
    'i18n_about_p3': 'Mai mult, cetățenii pot găsi informații despre aceste complexe care ar putea ajuta în deciziile lor zilnice, de ex. de unde să cumpere mâncare sănătoasă și locală. Dacă aveți nevoie de asistență în utilizarea site-ului web, aruncați o privire asupra diferitelor subiecte din bara de navigare din partea de sus a paginii. Desigur, puteți contacta și echipa de proiect pe adresa de email: <a href="mailto:iulian.nichersu@ddni.ro">iulian.nichersu@ddni.ro</a>',
    'i18n_about_p4': 'Vizualizări și analize mai complexe pot fi găsite aici (adăugați link). Există, de asemenea, o hartă a poveștii fiecarui oras studiu de caz din cadrul proiectului (adăugați link).',
    'i18n_food_p1': 'Alimentație',
    'i18n_food_p2': 'Pe acest site, puteți găsi și trimite informații despre mâncarea din Tulcea și împrejurimi.',
    'i18n_food_p3': 'Puteți adăuga producători de produse alimentare și servicii de producție cu punctele lor de vanzare și de depozitare.',
    'i18n_water_p1': 'Apă',
    'i18n_water_p2': 'Pe acest site, puteți găsi și trimite informații despre furnizorii de apă din Tulcea și din împrejurimi.',
    'i18n_energy_p1': 'Energie',
    'i18n_energy_p2': 'Pe acest site, puteți trimite informații despre utilizarea dvs. de energie.',
    'i18n_home': 'Acasă',
    'i18n_add': 'Adăugați',
    'i18n_edit': 'Editați',
    'i18n_submit': 'Înregistrează',
    'i18n_add_sale_point': 'Adaugă punct de vanzare',
    'i18n_sale_point_list': 'Lista punctelor de vânzare',
    'i18n_sale_point': 'Punct de vânzare',
    'i18n_show_sale_points': 'Arată puncte de vânzare',
    'i18n_this_sale_point': 'Acest punct de vânzare',
    'i18n_all_sale_points': 'Toate puncte de vânzare',
    'i18n_add_storage_point': 'Adaugă punct de depozitare',
    'i18n_storage_point_list': 'Listă puncte de depozitare',
    'i18n_storage_point': 'Puncte de stocare',
    'i18n_show_storage_points': 'Arată puncte de stocare',
    'i18n_this_storage_point': 'Acest punct de stocare',
    'i18n_all_storage_points': 'Toate puncte de stocare',
    'i18n_add_producer': 'Adaugă producător',
    'i18n_producer_list': 'Lista producătorilor',
    'i18n_show_producers': 'Arată producătorilor',
    'i18n_this_producer': 'Acest producător',
    'i18n_all_producers': 'Toate producătorilor',
    'i18n_producer': 'producător',
    'i18n_add_production_service': 'Adaugă servicii de producție',
    'i18n_production_service_list': 'Lista serviciilor de producție',
    'i18n_show_production_services': 'Arată serviciilor de producție',
    'i18n_this_production_service': 'Acest servicii de producție',
    'i18n_all_production_services': 'Toate serviciilor de producție',
    'i18n_production_service': 'servicii de producție',
    'i18n_add_consumer': 'Adaugă consumator',
    'i18n_consumer_list': 'Lista consumatorilor',
    'i18n_show_consumers': 'Arată consumatorilor',
    'i18n_consumer': 'consumator',
    'i18n_add_watersupplier': 'Adaugă furnizor de apă',
    'i18n_watersupplier_list': 'Lista furnizorilor de apă',
    'i18n_show_watersuppliers': 'Arată furnizorilor de apă',
    'i18n_this_watersupplier': 'Acest furnizor de apă',
    'i18n_all_watersuppliers': 'Toate furnizorilor de apă',
    'i18n_watersupplier': 'furnizor de apă',
    'i18n_add_energyusage': 'Adăugați consumul de energie',
    'i18n_energyusage_list': 'Lista consumurilor de energie',
    'i18n_show_energyusages': 'Arată consumurilor de energie',
    'i18n_this_energyusage': 'Acest consumul de energie',
    'i18n_all_energyusages': 'Toate consumurilor de energie',
    'i18n_energyusage': 'consumul de energie',
    'i18n_this_energy_usage': 'Acest consumul de energie',
    'i18n_add_feedback': 'Adaugă feedback',
    'i18n_feedback_list': 'Lista de feedback',
    'i18n_show_feedbacks': 'Arată feedbacks',
    'i18n_feedback': 'feedback',
    'i18n_general': 'Informații generale',
    'i18n_name': 'Nume',
    'i18n_type': 'Tip',
    'i18n_type_choices': [{'name': "certificate", 'label': "Deținător de certificat de producător"}, {'name': "small_company", 'label': "Companie mică"}, {'name': "small_gardening", 'label': "Producător local"}],
    'i18n_products': 'Produse principale',
    'i18n_contact': 'Contact',
    'i18n_address': 'Adresă',
    'i18n_telephone': 'Telefon',
    'i18n_email': 'E-mail',
    'i18n_website': 'Site web',
    'i18n_location': 'Locație',
    'i18n_location_mode': 'Mod locare',
    'i18n_toggle_choices': [{'name': "gps", 'label': "Folosește GPS"}, {'name': "interactive", 'label': "Punct pe hartă"}, {'name': "manual", 'label': "Introducere manuală"}],
    'i18n_latitude': 'Latitudine',
    'i18n_longitude': 'Longitudine',
    'i18n_accuracy': 'Acuratețe GPS',
    'i18n_yes': 'Da',
    'i18n_no': 'Nu',
    'i18n_water_energy': 'Apă și energie',
    'i18n_irrigation_use': 'Folosiți vreun sistem de irigatii?',
    'i18n_irrigation_use_choices': [{'name': "yes", 'label': "Da"}, {'name': "no",'label': "Nu"}],
    'i18n_water_quantity': 'Cantitatea de apă (în m³ pe an)',
    'i18n_water_quality': 'Calitatea apei',
    'i18n_irrigation_quality_choices': [{'name': "source", 'label': "Din sursă"}, {'name': "underground",'label': "Apă subterană"}],
    'i18n_irrigation_interest': 'Aveți interes să folosești apa pentru irigații?',
    'i18n_irrigation_interest_choices': [{'name': "yes", 'label': "Da"}, {'name': "no",'label': "Nu"}],
    'i18n_electrical_consumption': 'Consum mediu de electricitate (în kWh pe an)',
    'i18n_distance': 'Distanța: producție-depozitare-punct de vânzare',
    'i18n_distance_hint': 'Pentru a calcula distanța, puteți utiliza instrumentul de linie din harta de mai sus. Aveți grijă la modul de localizare "Punct pe hartă" este selectat. În acest caz, la trasarea unei linii, locația producătorului va fi schimbată. Pentru a evita acest lucru, puteți alege temporar "Introducere manuală" ca mod de localizare.',
    'i18n_production': 'Producție (în kg/ha pe an)',
    'i18n_surface': 'Suprafața cultivată (în ha)',
    'i18n_uses': 'Utilizări',
    'i18n_use_choices': [{'name': "homefood", 'label': "Uz casnic"}, {'name': "other",'label': "Alte utilizări alimentare"}],
    'i18n_fertilizer_use': 'Folosirea îngrășămintelor',
    'i18n_fertilizer_choices': [{'name': "natural", 'label': "Naturale"}, {'name': "artificial",'label': "Artificiale"}],
    'i18n_products_info': 'Informații legate de produse',
    'i18n_source_raw_material': 'Sursa materiei prime',
    'i18n_water_quantity_month': 'Cantitatea de apă (în m³ pe lună)',
    'i18n_energy_consumption': 'Consumul mediu de energie (în kWh pe lună)',
    'i18n_distance2': 'Distanța: servicii de producție-depozitare-punct de vânzare',
    'i18n_distance_hint2': 'Pentru a calcula distanța, puteți utiliza instrumentul de linie din harta de mai sus. Aveți grijă la modul de localizare "Punct pe hartă" este selectat. În acest caz, la trasarea unei linii, locația serviciului de producție va fi modificată. Pentru a evita acest lucru, puteți alege temporar "Introducere manuală" ca mod de localizare.',
    'i18n_covid_measures': 'Vă afectează măsurile luate în contextul limitării infecției cu COVID-19?',
    'i18n_covid_affected_choices': [{'name': "yes", 'label': "Da"}, {'name': "no",'label': "Nu"}],
    'i18n_effects': 'Efectul principal este',
    'i18n_main_effect_choices': [{'name': "scaderea_vanzarilor", 'label': "Scăderea vânzărilor"}, {'name': "scaderea_cifrei",'label': "Scăderea cifrei de afaceri"}, {'name': "disponibilizari",'label': "Disponibilizări"}, {'name': "intarzieri",'label': "Întârzieri la plata furnizorilor"}, {'name': "dificultati",'label': "Dificultăţi la încasare"}, {'name': "restrangerea",'label': "Restrângerea activității"}, {'name': "suspendarea",'label': "Suspendarea temporară a activităţii"}, {'name': "inchiderea",'label': "Închiderea firmei"}, {'name': "reprofilare",'label': "Reprofilare"}],
    'i18n_turnover_decrease': 'Care este procentul cu care estimați scăderea cifrei de afaceri?',
    'i18n_gender': 'Sex',
    'i18n_gender_choices': [{'name': "male", 'label': "Masculin"}, {'name': "female",'label': "Feminin"}],
    'i18n_age': 'Vârsta',
    'i18n_income': 'Venit (euro)',
    'i18n_income_choices': [{'name': "less_1500", 'label': "Sub 1500/per membru de familie"}, {'name': "more_1500",'label': "Peste 1500/per membru de familie"}, {'name': "na",'label': "Nu doresc sa răspund"}],
    'i18n_consumer_profile': 'Profilul consumatorului',
    'i18n_source_raw_aliments': 'Sursa alimentelor (selectați numărul de aprovizionări pe săptamână)',
    'i18n_big_store': 'Lanț de magazine național',
    'i18n_big_chain_store_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "cca 3"}, {'name': "more",'label': "Mai multe"}],
    'i18n_local_store': 'Lanț local de magazine',
    'i18n_local_chain_store_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "cca 3"}, {'name': "more",'label': "Mai multe"}],
    'i18n_small_shop': 'Magazin mic',
    'i18n_small_shop_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "cca 3"}, {'name': "more",'label': "Mai multe"}],
    'i18n_market': 'Piața agroalimentară',
    'i18n_market_choices': [{'name': "1", 'label': "1"}, {'name': "3",'label': "cca 3"}, {'name': "more",'label': "Mai multe"}],
    'i18n_main_transport': 'Transport principal',
    'i18n_transport_choices': [{'name': "car", 'label': "Auto personal"}, {'name': "public",'label': "Transport public"}, {'name': "bike",'label': "Bicicletă"}, {'name': "foot",'label': "Pedestru"}],
    'i18n_bio_use': 'Folosirea produselor bio',
    'i18n_bio_choices': [{'name': "frequently", 'label': "Frecvent"}, {'name': "sometimes",'label': "Uneori"}, {'name': "no_use",'label': "Niciodata"}],
    'i18n_product_origin': 'Folosirea produselor locale/nationale',
    'i18n_local_choices': [{'name': "frequently", 'label': "Frecvent"}, {'name': "sometimes",'label': "Uneori"}, {'name': "no_use",'label': "Niciodata"}],
    'i18n_tap_water': 'Cantitatea de apă de  robinet utilizată (în m³)',
    'i18n_bottled_water': 'Cantitatea de apă îmbuteliată utilizată (în m³)',
    'i18n_waste_water': 'Apă menajeră (sistem folosit)',
    'i18n_waste_water_choices': [{'name': "sewage", 'label': "Sistem centralizat de canalizare"}, {'name': "septic", 'label': "Fosă septică"}, {'name': "no_treatment",'label': "Nici unul"}],
    'i18n_food_priorization': 'Priorități în alegerea alimentelor',
    'i18n_priorization_choices': [{'name': "price", 'label': "Prețul"}, {'name': "ecological_impact",'label': "Impactul ecologic"}, {'name': "aquisition_time",'label': "Timpul consumat pentru cumpărături(distanța până la magazin)"}, {'name': "health_impact",'label': "Impactul asupra sănătății"}],
    'i18n_location_headquarters': 'Locația sediului',
    'i18n_water_supply': 'Sursa de apă',
    'i18n_bogza': 'Bogza (în m³)',
    'i18n_mila': 'Mila (în m³)',
    'i18n_irrigation_supply': 'Sursă irigații',
    'i18n_irrigation_supply_choices': [{'name': "source", 'label': "Din sursă"}, {'name': "underground",'label': "Apă subterană"}],
    'i18n_energy_type': 'Ce tip de energie folosiți?',
    'i18n_energy_type_choices': [{'name': "national", 'label': "Sistem Național"}, {'name': "renewable",'label': "Regenerabilă"}, {'name': "both", 'label': "Amândouă"}],
    'i18n_more_renewable': 'Vați dori să folosiți mai multă energie regenerabilă?',
    'i18n_more_renewable_choices': [{'name': "yes", 'label': "Da"}, {'name': "no",'label': "Nu"}],
    'i18n_type_renewable': 'Ce tip de energie regenerabilă folosiți?',
    'i18n_renewable_type_choices': [{'name': "solar", 'label': "Solar"}, {'name': "wind",'label': "Vânt"}, {'name': "water", 'label': "Apă"}, {'name': "geothermal", 'label': "Geotermală"}, {'name': "bio", 'label': "Bio"}, {'name': "other", 'label': "Alte"}],
    'i18n_renewable_hint': 'Vă rugăm să adăugați locația sursei de energie regenerabilă pe care o utilizați. <br> <br> Puteți alege între trei opțiuni pentru setarea locației. În prima opțiune, locația este preluată de pe GPS-ul dispozitivului dvs. (dacă este disponibil). Ca a doua opțiune, puteți face clic pe harta de mai jos, iar ca a treia opțiune puteți introduce latitudinea și longitudinea direct în câmpurile de mai jos. Ultima opțiune este recomandată numai utilizatorilor experimentați.',
    'i18n_useful': 'Această aplicație este folositoare',
    'i18n_usability_choices': [{'name': "strong_agree", 'label': "Total de acord"}, {'name': "rather_agree",'label': "De acord"}, {'name': "undecided",'label': "Indecis"}, {'name': "rather_disagree",'label': "Nu sunt de acord"}, {'name': "strong_disagree",'label': "Dezacord total"}],
    'i18n_attractive': 'Aplicația este atractivă din punct de vedere vizual (grafic)',
    'i18n_attractiveness_choices': [{'name': "strong_agree", 'label': "Total de acord"}, {'name': "rather_agree",'label': "De acord"}, {'name': "undecided",'label': "Indecis"}, {'name': "rather_disagree",'label': "Nu sunt de acord"}, {'name': "strong_disagree",'label': "Dezacord total"}],
    'i18n_maps_helpful': 'Hărțile ajută la folosirea aplicației',
    'i18n_maps_choices': [{'name': "strong_agree", 'label': "Total de acord"}, {'name': "rather_agree",'label': "De acord"}, {'name': "undecided",'label': "Indecis"}, {'name': "rather_disagree",'label': "Nu sunt de acord"}, {'name': "strong_disagree",'label': "Dezacord total"}],
    'i18n_clear_instruction': 'Instrucțiunile de folosire ale aplicației sunt ușor de înțeles',
    'i18n_clarity_choices': [{'name': "strong_agree", 'label': "Total de acord"}, {'name': "rather_agree",'label': "De acord"}, {'name': "undecided",'label': "Indecis"}, {'name': "rather_disagree",'label': "Nu sunt de acord"}, {'name': "strong_disagree",'label': "Dezacord total"}],
    'i18n_main_attraction': 'Care a fost principala atracție?',
    'i18n_additional_functions': 'Ce alte funcții ar trebui incluse în aplicație?',
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
