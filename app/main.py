import utils # al importarlo podemos comenzar a ejecutarlo
import read_csv
import charts

def run() :
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type your country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0 :
    country = result[0] #para tomar la primera lista que me mande, que en si solo deberia mandarme una :v
    lebels, values = utils.get_population(country)
    charts.generate_bar_chart(lebels, values)
  
  # Esto se conoce como modulizar nuestra app y poder reutilizar código desde archivos
  #print(result)

def run_2 ():
  data = read_csv.read_csv('./app/data.csv')
  column = input('Typethe column you want a pie chart => ')

  lebels, values = utils.get_column(data, column)
  if len(values) > 0 :
    charts.generate_pie_chart(lebels, values)

  
# Ejecutarllo como scrip y como módulo
if __name__ == '__main__' : 
  #run()
  run_2 ()