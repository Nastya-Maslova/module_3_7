def calculate_structure_sum(*args):
  summ_ = 0
  for i in args:
      if isinstance(i, (int, float)):
          summ_+= i
      elif isinstance(i,str):
          summ_+=len(i)
      elif isinstance(i,(list,tuple,set)):
          summ_+=calculate_structure_sum(*i)
      elif isinstance(i,dict):
          summ_+=calculate_structure_sum(*i.keys(),*i.values())
  return summ_

data_structure=[
    [1,2,3], {"a":4,"b":5},
    (6,{"cube":7,"drum":8}), "Hello",
    ((),[{(2,"Urban", ("Urban2",35))}])]
result= calculate_structure_sum(data_structure)
print(result)

