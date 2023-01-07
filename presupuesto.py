#P = presupuesto final 
#P1 = presupuesto 1
#P1 = presupuesto 2
#P1 = presupuesto 3
#P1 = presupuesto 4

#CA1= Conpras del Almacen 1
#CA2= Conpras del Almacen 2
#CA3= Conpras del Almacen 3
#CA4= Conpras del Almacen 4

#V1 =Ventas del Almacen 1
#V2 =Ventas del Almacen 2
#V3 =Ventas del Almacen 3
#V4 =Ventas del Almacen 4

#PE = Pagos de empleados

def presupuestoTotal (P):

    def run () :

        P =(p1 + p2 + p3 + p4)
        p1 =(CA1 + p4 * V1)
        p2 =(CA2 * V2)
        p3 =(CA3 * PE)
        p4 =(CA4 * PE + V3)

        CA1 =str(input ("esciba las compras hechas por el almacen almacen #1") ) 
        CA2 =str(input ("esciba las compras hechas por el almacen almacen #2") )
        CA3 =str(input ("esciba las compras hechas por el almacen almacen #3") )
        CA4 =str(input ("esciba las compras hechas por el almacen almacen #4") )

        V1 =str( input ("Total de ventas hechas por el almacen #1") )
        V2 =str( input ("Total de ventas hechas por el almacen #2") )
        V3 =str( input ("Total de ventas hechas por el almacen #3") )
        V4 =str( input ("Total de ventas hechas por el almacen #4") )

        PE =str(input ("Pago total a empleados ") )

    if __name__ == "__main__":

        run()
