import numpy as np

def calculate(list):
    if len(list) == 9:
       list= np.array(list)
       list= list.reshape(3,3)
       calculations = {
      'mean': [[list[:,0].mean(),list[:,1].mean(),list[:,2].mean()],[list[0,:].mean(),list[1,:].mean(),list[2,:].mean()], list.mean()],
      'variance': [[list[:,0].var(),list[:,1].var(),list[:,2].var()],[list[0,:].var(),list[1,:].var(),list[2,:].var()], list.var()],
      'standard deviation': [[list[:,0].std(),list[:,1].std(),list[:,2].std()],[list[0,:].std(),list[1,:].std(),list[2,:].std()], list.std()],
      'max': [[list[:,0].max(),list[:,1].max(),list[:,2].max()],[list[0,:].max(),list[1,:].max(),list[2,:].max()], list.max()],
      'min': [[list[:,0].min(),list[:,1].min(),list[:,2].min()],[list[0,:].min(),list[1,:].min(),list[2,:].min()], list.min()],
      'sum': [[list[:,0].sum(),list[:,1].sum(),list[:,2].sum()],[list[0,:].sum(),list[1,:].sum(),list[2,:].sum()], list.sum()]
    } 
       return calculations
    
    else:
        
        raise ValueError('List must contain nine numbers.')

    