# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:50:21 2023

@author: beatr
"""

tamaños_I = [168, 270, 500, 900, 1500] #Hasta aquí puede bien el modelo
tamaños_L = [16, 50, 100]
tamaños_S = [10, 50, 100, 150, 200]

##tamaños_I = [900] 
##tamaños_L = [50]
##tamaños_S = [100]

# tamaños_I = [168] 
# tamaños_L = [16]
# tamaños_S = [10]

rates = [0.4]
verif = 0.4

#ambulance = [[10, 6], [20,11], [35,20]]
ambulance = [[35,20]]

for iconj in range(len(tamaños_I)):
    for jconj in range(len(tamaños_L)):
        for sconj in range(len(tamaños_S)):
            for k in range(len(ambulance)):
            #for rep in range(repeticiones):
                
                eta = ambulance[k]

                archivo = open('Resultados_Prueba_FirstModel_Modified_210924_'
                          +str(tamaños_I[iconj])+str('_')
                          +str(tamaños_L[jconj])+str('_')
                          +str(tamaños_S[sconj])
                          +'_'+str(eta[0])+'_'+str(eta[1])
                          +'.txt', "r")
                
                line = archivo.readline().strip().split()
                line = archivo.readline().strip().split()
                
                f = open ('Location_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                for i in range(tamaños_L[jconj]*2):
                    line = archivo.readline()
                    f.write(line)
                    
                f.close()
                
                
                line = archivo.readline()
                g = open ('Dispatch_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while len(line) > 15:
                    g.write(line)
                    line = archivo.readline()
                        
                g.close()
                
                
                h = open ('Full_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while "Total" in line and "Total late" not in line:
                    h.write(line)
                    line = archivo.readline()
                        
                h.close()
                
                o = open ('Partial1_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while "Total late" in line:
                    o.write(line)
                    line = archivo.readline()
                        
                o.close()
                
                
                p = open ('Partial2_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while "Partial" in line and "Partial late" not in line:
                    p.write(line)
                    line = archivo.readline()
                        
                p.close()
                
                
                q = open ('Partial3_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while "Partial late" in line:
                    q.write(line)
                    line = archivo.readline()
                        
                q.close()
                    
                
                r = open ('Null_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'_'+str(eta[0])+'_'+str(eta[1])+'.txt','w')
                
                while "Null" in line:
                    r.write(line)
                    line = archivo.readline()
                        
                r.close()
                
                # verif=0.4
                h = open('Instances_DemandFixed_'
                          +str(tamaños_I[iconj])+str('_')
                          +str(tamaños_L[jconj])+str('_')
                          +str(tamaños_S[sconj])
                          + '_' + str(verif) + '_'
                          +'.txt', "r")
                
                line_1 = h.readline()
                line_1 = h.readline()
                line_1 = h.readline()
                
                for cant in range(tamaños_S[sconj]):
                    line_1 = h.readline()
                
                
                un = open ('ScAccidents_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'.txt','w')
                
                u = open ('Accidents_FirstModel_Modified_210924_'
                              +str(tamaños_I[iconj])+str('_')
                              +str(tamaños_L[jconj])+str('_')
                              +str(tamaños_S[sconj])+'.txt','w')
                        
                
                accidentes = []
                for cant in range(tamaños_S[sconj]):
                    line_1 = h.readline().strip().split()
                    un.write(str(line_1))
                    accident = 0
                    total_accidents = 0
                    for a in range(tamaños_I[iconj]):
                        if int(line_1[accident])!=0 or int(line_1[accident+1])!=0:
                            total_accidents += 1 
                        accident += 2
                    accidentes.append(total_accidents)
                    u.write(str(total_accidents))
                    u.write(' ')
                
                u.close()
                    
                un.close()
                
                    
                    
                # # u = open ('Accidents_ObjZs_Scenarios_'
                # #               +str(tamaños_I[iconj])+str('_')
                # #               +str(tamaños_L[jconj])+str('_')
                # #               +str(tamaños_S[sconj])+'.txt','w')
                        
                
                # # accidentes = []
                # # for cant in range(tamaños_S[sconj]):
                # #     line_1 = h.readline().strip().split()
                # #     accident = 0
                # #     total_accidents = 0
                # #     for a in range(tamaños_I[iconj]):
                # #         if int(line_1[accident])!=0 or int(line_1[accident+1])!=0:
                # #             total_accidents += 1 
                # #         accident += 2
                # #     accidentes.append(total_accidents)
                # #     u.write(str(total_accidents))
                # #     u.write(' ')
                
                # # u.close()
                
                # tim = open ('rli_FirstModel_Modified_210924_'
                #               +str(tamaños_I[iconj])+str('_')
                #               +str(tamaños_L[jconj])+str('_')
                #               +str(tamaños_S[sconj])+'.txt','w')
                
                # for cant in range(tamaños_L[jconj]):
                #     line_1 = h.readline()
                #     tim.write(line_1)
                    
                # v = open ('Cli_FirstModel_Modified_210924_'
                #               +str(tamaños_I[iconj])+str('_')
                #               +str(tamaños_L[jconj])+str('_')
                #               +str(tamaños_S[sconj])+'.txt','w')
                    
                # for cant in range(tamaños_L[jconj]):
                #     line_1 = h.readline()
                #     v.write(line_1)
                    
                # v.close()
                    
                
                        
                
