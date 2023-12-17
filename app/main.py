import utils # al importarlo podemos comenzar a ejecutarlo
import read_csv
import charts
import pandas as pd

def run() :
  data = read_csv.read_csv('data.csv') 
  '''Estas funcionalidades ya nos las ahorramos con Pandas
  data = list(filter(lambda item : item['Continent'] == 'South America', data))

  contries = list(map(lambda x : x ['Country/Territory'],data ))
  percentages = list(map(lambda x : x ['World Population Percentage'], data))
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa' ]

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  country = input('Type your country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0 :
    country = result[0] #para tomar la primera lista que me mande, que en si solo deberia mandarme una :v
    print(country)
    lebels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],lebels, values)
  
  # Esto se conoce como modulizar nuestra app y poder reutilizar código desde archivos
  #print(result)

"""def run_2 ():
  data = read_csv.read_csv('./app/data.csv')
  column = input('Typethe column you want a pie chart => ')

  lebels, values = utils.get_column(data, column)
  if len(values) > 0 :
    charts.generate_pie_chart(lebels, values)"""

  
# Ejecutarlo como scrip y como módulo
if __name__ == '__main__' : 
  run()
  #run_2 ()