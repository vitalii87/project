class PulseEmployee:
  title="Infopullse Imployee"

  def __init__(self,name='',surename='',position='', salary=0, ):
        self.name = name.title()
        self.surname = surename.title()
        self.position= position.title()
        self.salary= salary


  def set_name(self, name):
        self.name = name

  def fullname(self):
        return self.name+' '+self.surname

  def income (self, months):
        return self.salary * months

  def increase_salary (self, addition):
        self.salary +=addition

if __name__=='__main__':
    e=PulseEmployee(surename='black',position='some', salary=100 )
    e.set_name('Dima')
    print(e.name, e.surname, e.position)
    print(e.fullname())
    print(e.increase_salary(400))
    print(e.salary)