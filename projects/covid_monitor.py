from covid import Covid

covid = Covid()
data = covid.get_status_by_country_id(142)

print (data)