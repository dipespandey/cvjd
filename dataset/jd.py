import pandas as pd

chef = ['chef', 'food', 'menu', 'gallery', 'galley', 'meal', 'dietary', 'diet', 'hygiene', 'hotel', 'restaurant', 'resort', 'cruise', 'guest', 'health', 'sanitation', 'cook', 'cooking', 'allergy', 'allergies', 'storage']
head_chef = ['chef', 'head chef', 'galley', 'gallery', 'menu', 'food', 'meal', 'dietary', 'diet', 'hygiene', 'hotel', 'restaurant', 'resort', 'cruise', 'guest', 'health', 'sanitation', 'cook', 'cooking', 'allergy', 'allergies', 'storage']
sous_sec_chef = ['chef', 'sous', 'second chef', 'galley', 'gallery', 'menu', 'food', 'meal', 'dietary', 'diet', 'hygiene', 'hotel', 'restaurant', 'resort', 'cruise', 'guest', 'health', 'sanitation', 'cook', 'cooking', 'allergy', 'allergies', 'storage']
crew_chef = ['chef', 'crew chef', 'galley', 'gallery', 'menu', 'food', 'meal', 'dietary', 'diet', 'hygiene', 'hotel', 'restaurant', 'resort', 'cruise', 'guest', 'health', 'sanitation', 'cook', 'cooking', 'allergy', 'allergies', 'storage']
captain = ['captain', 'chief mate', 'superyacht', 'crew', 'manning', 'operation', 'vessel', 'yacht', 'owner', 'guests', 'personnel', 'management', 'shipyard', 'project', 'legal', 'regulatory', 'accounting', 'decisions', 'operations', 'department', 'nautical', 'maintenance', 'leadership', 'communication', 'administrative', 'paperwork']
first_officer = ['captain', 'first officer', 'chief mate', 'superyacht', 'crew', 'manning', 'operation', 'vessel', 'yacht', 'owner', 'guests', 'personnel', 'management', 'shipyard', 'project', 'legal', 'regulatory', 'accounting', 'decisions', 'operatoins', 'department', 'nautical', 'maintenance', 'leadership', 'communication', 'administrative', 'paperwork']
second_officer = ['captain', 'chief mate', 'second officer', 'superyacht', 'crew', 'manning', 'operation', 'vessel', 'yacht', 'owner', 'guests', 'personnel', 'management', 'shipyard', 'project', 'legal', 'regulatory', 'accounting', 'decisions', 'operatoins', 'department', 'nautical', 'maintenance', 'leadership', 'communication', 'administrative', 'paperwork']
third_officer = ['captain', 'chief mate', 'third officer', 'superyacht', 'crew', 'manning', 'operation', 'vessel', 'yacht', 'owner', 'guests', 'personnel', 'management', 'shipyard', 'project', 'legal', 'regulatory', 'accounting', 'decisions', 'operatoins', 'department', 'nautical', 'maintenance', 'leadership', 'communication', 'administrative', 'paperwork']
bosun = ['bosun', 'deckhand', 'deck', 'operations', 'guests', 'owners', 'board', 'detail', 'service', 'tender', 'driver', 'toys', 'passerelle', 'security', 'embark', 'embarking', 'vehicles', 'equipments', 'mechanised', 'devices', 'watches', 'painting', 'varnishing', 'storage', 'engineering']
deckhand = ['bosun', 'deckhand', 'deck', 'operations', 'guests', 'owners', 'board', 'detail', 'service', 'tender', 'driver', 'toys', 'passerelle', 'security', 'embark', 'embarking', 'vehicles', 'equipments', 'mechanised', 'devices', 'watches', 'painting', 'varnishing', 'storage', 'engineering', 'cleanliness', 'boat', 'tenders', 'interior']
lead_deckhand = ['bosun', 'deckhand', 'lead deckhand', 'deck', 'operations', 'guests', 'owners', 'board', 'detail', 'service', 'tender', 'driver', 'toys', 'passerelle', 'security', 'embark', 'embarking', 'vehicles', 'equipments', 'mechanised', 'devices', 'watches', 'painting', 'varnishing', 'storage', 'engineering']
purser = ['purser', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
chief_steward = ['purser', 'chief steward', 'steward', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
steward = ['purser', 'steward', 'stewardess', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
stewardess = ['purser', 'stewardess', 'steward', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
second_steward = ['purser',  'steward', 'second steward', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
service_steward = ['purser', 'steward', 'service steward', 'administrative', 'management', 'inventory', 'purchasing', 'accounting', 'guest activities', 'paperwork', 'finance', 'financial', 'computer', 'communication', 'delegation', 'recruiting', 'recruit', 'trainig', 'detail', '7-star', 'silver service', 'accomodation', 'cabin', 'trips', 'transport']
chief_engineer = ['engineer', 'chief engineer', 'engine', 'electrical', 'engineering', 'technical', 'troubleshoot', 'repair', 'liaising', 'mechanical', 'jet ski', 'television', 'engine room']
second_engineer = ['engineer', 'second engineer', 'engine', 'electrical', 'engineering', 'technical', 'troubleshoot', 'repair', 'liaising', 'mechanical', 'jet ski', 'television', 'engine room']
third_engineer = ['engineer', 'third engineer', 'engine', 'electrical', 'engineering', 'technical', 'troubleshoot', 'repair', 'liaising', 'mechanical', 'jet ski', 'television', 'engine room'] 
fourth_engineer = ['engineer', 'fourth engineer', 'engine', 'electrical', 'engineering', 'technical', 'troubleshoot', 'repair', 'liaising', 'mechanical', 'jet ski', 'television', 'engine room']
eto = ['av', 'it', 'electronic', 'computer', 'audio', 'visual', 'radio', 'radar', 'telephone', 'satellite', 'navigation', 'computer', 'tv', 'dvd']
electrician = ['electrician', 'electric', 'electronic', 'circuit board', 'breaker', 'switch', 'lighting', 'batteries', 'computer', 'audio', 'visual', 'radio', 'radar', 'telephone', 'satellite', 'navigation', 'computer', 'tv', 'dvd']
avit = ['av', 'it', 'electronic', 'computer', 'audio', 'visual', 'radio', 'radar', 'telephone', 'satellite', 'navigation', 'computer', 'tv', 'dvd']

dict_of_jobs = {}
dict_of_jobs['chef'] = chef
dict_of_jobs['head_chef'] = head_chef                                                                                                               
dict_of_jobs['sous_sec_chef'] = sous_sec_chef                                                                                                      
dict_of_jobs['crew_chef'] = crew_chef                                                                                                              
dict_of_jobs['captain'] = captain                                                                                                                  
dict_of_jobs['first_officer'] = first_officer                                                                                                      
dict_of_jobs['second_officer'] = second_officer                                                                                                    
dict_of_jobs['third_officer'] = third_officer                                                                                                      
dict_of_jobs['bosun'] = bosun                                                                                                                      
dict_of_jobs['deckhand'] = deckhand                                                                                                                
dict_of_jobs['lead_deckhand'] = lead_deckhand                                                                                                      
dict_of_jobs['purser'] = purser                                                                                                                    
dict_of_jobs['chief_steward'] = chief_steward                                                                                                      
dict_of_jobs['steward'] = steward   
dict_of_jobs['stewardess'] = stewardess   
dict_of_jobs['second_steward'] = second_steward   
dict_of_jobs['chief_engineer'] = chief_engineer  
dict_of_jobs['second_engineer'] = second_engineer   
dict_of_jobs['third_engineer'] = third_engineer   
dict_of_jobs['fourth_engineer'] = fourth_engineer  
dict_of_jobs['eto'] = eto   
dict_of_jobs['electrician'] = electrician   
dict_of_jobs['avit'] = avit   


df_jd = pd.DataFrame()
for i in dict_of_jobs:
    df = pd.DataFrame.from_dict({i:pd.Series(dict_of_jobs[i])})
    df_jd = pd.concat([df_jd, df], axis=1)
print(df_jd.shape)