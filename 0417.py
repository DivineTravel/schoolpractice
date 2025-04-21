import time
import random

capital = ['''Abidjan, Abu Dhabi, Abuja, Accra, Addis Ababa, Algiers, Alofi, Amman, Amsterdam, Andorra la Vella, Ankara, 
           Antananarivo, Apia, Ashgabat, Asmara, Astana, Athens, Avarua, Baghdad, Baku, Bamako, Bandar Seri Begawan, 
           Bangkok, Bangui, Banjul, Basseterre, Beijing, Beirut, Belgrade, Belmopan, Berlin, Bern, Bishkek, Bissau, Bloemfontein,
            Bogota, Brasilia, Bratislava, Brazzaville, Bridgetown, Brussels, Bucharest, Budapest, Buenos Aires, Cairo, Canberra, 
           Cape Town, Caracas, Castries, Chișinău, Colombo, Conakry, Copenhagen, Dakar, Damascus, Dhaka, Dili, Djibouti, Dodoma,
            Doha, Dublin, Dushanbe, Funafuti, Gaborone, Georgetown, Gitega, Guatemala City, Hanoi, Harare, Havana, Helsinki,
            Honiara, Islamabad, Jakarta, Jerusalem, Juba, Kabul, Kampala, Kathmandu, Khartoum, Kyiv, Kigali, Kingstown, Kinshasa,
            Kuala Lumpur, Kuwait City, La Paz, Libreville, Lilongwe, Lima, Lisbon, Ljubljana, Lobamba, Lomé, London, Luanda, 
           Lusaka, Luxembourg, Madrid, Majuro, Malabo, Managua, Manama, Manila, Maputo, Maseru, Mbabane, Melekeok, 
           Mexico City, Minsk, Mogadishu, Monaco, Monrovia, Montevideo, Moroni, Moscow, Muscat, Nairobi, Nassau, 
           Naypyidaw, New Delhi, Ngerulmud, Niamey, Nicosia, Nouakchott, Ottawa, Ouagadougou, Palikir, Panama City, 
           Paramaribo, Paris, Phnom Penh, Podgorica, Port Louis, Port Moresby, Port of Spain, Port-au-Prince, Port Vila, 
           Porto-Novo, Prague, Praia, Pretoria, Pristina, Putrajaya, Pyongyang, Quito, Rabat, Reykjavík, Riga, Riyadh, Rome, 
           Roseau, San Jose, San Marino, San Salvador, Sana'a, Santiago, Santo Domingo, Sarajevo, Seoul, Singapore, Skopje, Sofia,
            Stockholm, Sucre, Suva, Taipei, Tallinn, Tarawa, Tashkent, Tbilisi, Tegucigalpa, Tehran, The Hague, Thimphu, Tirana, Tokyo, Tripoli, Tunis, Ulaanbaatar, Vaduz, Valletta, Vatican City, 
           Victoria, Vienna, Vientiane, Vilnius, Warsaw, Washington D.C., Wellington, Windhoek, Yamoussoukro, Yerevan, Zagreb
           ''']
capital = capital[0].split(''', ''')  

correct = 0
total = 0
start_time = time.time()
end_time = start_time + 60 

print("You have 1 minute to answer as many capitals as possible!")
while time.time() < end_time and capital:
    n = random.randint(0, len(capital) - 1)
    word = capital.pop(n)  
    print("Capital:", word)
    user = input("Your answer: ")
    total += 1
    if user == word:
        print("Correct!")
        correct += 1
    else:
        print("Wrong!")

success_rate = round((correct / total) * 100, 2) if total > 0 else 0
speed = round(total / 1, 2)  

print("\nTime's up!")
print("Total questions answered:", total)
print("Correct answers:", correct)
print("Success rate:", success_rate, "%")
print("Speed:", speed, "capitals per minute")
