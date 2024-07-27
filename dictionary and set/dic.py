countries_and_their_famous_places={
    "Nepal":"basantapur",
    "India":"tajmahal",
    "Thailand":"bankok",
    "spain":"madrid"
}
# print(countries_and_their_famous_places,type(countries_and_their_famous_places))
# for places in countries_and_their_famous_places:
# #     print(places)
# print(countries_and_their_famous_places.keys())
# print(countries_and_their_famous_places.values())
# countries_and_their_famous_places.update({"Nepal":"nuwakot"})
# print(countries_and_their_famous_places)
# print(countries_and_their_famous_places.items())
# print(countries_and_their_famous_places["India"])

#if we use get then no error
# countries_and_their_famous_places.clear()
countries_and_their_famous_places.pop("Nepal")
print(len(countries_and_their_famous_places))

print(countries_and_their_famous_places)