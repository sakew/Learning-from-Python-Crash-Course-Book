"""Function that stores information about City"""

def city_info(city_name, country_name, population = 0):

    output = city_name.title() + ', ' + country_name.title()

    if population:

        output = output + ' - population ' + str(population)



    return(output)

