capitals={"France":"Paris",
          "Germany":"Berlin",}
#Nesting a list in a Dictionary
travel_log={"France":["Paris","Lille","Dijon"],
            "Germany":["Berling","Leverkusen","Hamburg"]}
print(travel_log["France"])
#Nesting Dictionary in a Dictionary
travel_log={"France":{"cities_visited":["Paris","Lille","Dijon"],"total_visited":12},
            "Germany":{"cities_visited":["Berling","Leverkusen","Hamburg"],"total_visited":9}}
print(travel_log["France"]["total_visited"])
print(travel_log["France"]["cities_visited"][1])
travel_log= [
{
     "country":"France",
     "cities_visited":["Paris","Lille","Dijon"],
     "total_visited":12
 },
 {
   "country":"Germany",
   "cities_visited":["Berlin","Leverkusen","Hamburg"],
    "total_visited":9
 }
 ]
print(travel_log[0]["cities_visited"])
print(travel_log[0]["country"])