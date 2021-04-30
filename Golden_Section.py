import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import sympy as sy
sns.set()


def golden_method(f,xx, rng = 1):
    
    number_of_itr = np.ceil((np.log(rng/2))/(np.log(1-ro))).astype('int32')
    
    tail , head= xx[0], xx[-1]
    
    a_new = tail + ro*(head- tail)
    b_new = tail + (1-ro)*(head - tail)
    
    
    for _ in range(number_of_itr): 
        
        f_anew = f.subs(x, a_new)
        f_bnew = f.subs(x, b_new)
        
        if f_anew < f_bnew : 
            
            tail = tail
            head = b_new
           
            b_new = a_new
            a_new = tail + ro*(head - tail)
            
        else:
            
            head = head 
            tail = a_new
            
            a_new = b_new
            b_new = tail + (1-ro)*(head - tail)
           

    return tail , head
  
  
if __name__ == "__main__":
  
  x = sy.Symbol('x')
 # f is the function we want to estimate where is its minimum point #  
  f = x**4 - 14*x**3 + 60*x**2 - 70*x

  ro = (3-np.sqrt(5))/ 2
  
  xx = np.linspace(0, 2, 200)
  yy = np.zeros_like(xx)
  
  for i in range(xx.size):
    yy[i] = f.subs(x, xx[i])
  
  #plot of the function with point a and point b 
  plt.figure(figsize=(8, 6))
  plt.plot(xx, yy, linewidth=2.5)
  plt.plot(xx[0], yy[0], '.r',xx[-1], yy[-1], '.r', markersize=12)
  plt.text(2,13,'b0', fontsize=13)
  plt.text(0.05,10,'a0', fontsize=13)
  plt.axvline(color='black'), plt.axhline(color='black')
  plt.pause(2)
  
 
  rng = 0.01
  a, b = golden_method(f, xx, rng)

  t = np.logical_and(xx > a , xx < b)
  xt = xx[t]
  yt = yy[t]

  plt.figure(figsize=(8, 6))
  plt.plot(xx, yy, linewidth=2.5)
  plt.axvline(color='black'), plt.axhline(color='black')
  plt.plot(a, f.subs(x, a), '.r', b, f.subs(x, b), '.r', markersize=15)
  plt.text(0.1, 10,  f'b - a = { np.round(b-a, 3)} < {rng}',fontsize=25)

 