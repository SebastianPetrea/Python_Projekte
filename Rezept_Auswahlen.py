_input = int(input('[1]Pfannkuchen \n[2]Wafelln \n[3]Kasekuchen \n-Welches Rezept mochten Sie Kochen?'))

if _input ==1:
    print('Pfannkuchen Rezept:','\n1 Eier', '\n100g Mehl','\n50ml Milch')   
elif _input ==2:
    print('Wafelln Rezept:','\n2 Eier', '\n150g Mehl','\n100ml Milch','\n25g Zucker') 
else:
    print('Kasekuchen Rezept:','\n5 Eier', '\n250g Mehl','\n250ml Milch','\n75g Zucker', '\n200g Quark') 
