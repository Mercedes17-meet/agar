import meet

user_cell={'radius':18,'x':20,'y':3,'dx':1,'dy':1,'color':'red','shape':'circle'}
cell1={'radius':17,'x':21,'y':5,'dx':2,'dy':-2,'color':'orange','shape':'circle'}
cell2={'radius':16,'x':22,'y':7,'dx':1,'dy':-1,'color':'blue','shape':'circle'}
cell3={'radius':15,'x':23,'y':56,'dx':2,'dy':1,'color':'green','shape':'circle'}
cell4={'radius':14,'x':24,'y':56,'dx':2,'dy':2,'color':'yellow','shape':'circle'}
cell5={'radius':13,'x':25,'y':345,'dx':2,'dy':1,'color':'black','shape':'circle'}
cell6={'radius':12,'x':26,'y':34,'dx':1,'dy':2,'color':'purple','shape':'circle'}
cell7={'radius':11,'x':27,'y':54,'dx':1,'dy':3,'color':'pink','shape':'circle'}
cell8={'radius':10,'x':28,'y':46,'dx':3,'dy':-3,'color':'brown','shape':'circle'}
cell9={'radius':9,'x':29,'y':46,'dx':-3,'dy':1,'color':'red','shape':'circle'}
Cells=[]
user_cell=meet.create_cell(user_cell)
Cells.append(user_cell)
cell=meet.create_cell(cell1)
Cells.append(cell)
cell=meet.create_cell(cell2)
Cells.append(cell)
cell=meet.create_cell(cell3)
Cells.append(cell)
cell=meet.create_cell(cell4)
Cells.append(cell)
cell=meet.create_cell(cell5)
Cells.append(cell)
cell=meet.create_cell(cell6)
Cells.append(cell)
cell=meet.create_cell(cell7)
Cells.append(cell)
cell=meet.create_cell(cell8)
Cells.append(cell)
cell=meet.create_cell(cell9)
Cells.append(cell)

def border_line(cells):
        for cell in Cells:
                if(cell.xcor()+cell.get_radius()> meet.get_screen_width() or cell.xcor() - cell.get_radius()< -meet.get_screen_width()):
                        cell.set_dx(-cell.get_dx())
                if(cell.ycor()+cell.get_radius()>meet.get_screen_height() or cell.ycor() -cell.get_radius()< -meet.get_screen_height()):
                        cell.set_dy(-cell.get_dy())
                
                  
flag = True
while flag:


        border_line(Cells)
        
        x, y=meet.get_user_direction(user_cell)
        user_cell.set_dy(y)
        user_cell.set_dx(x)
        meet.move_cells(Cells)
        
        

meet.mainloop()

