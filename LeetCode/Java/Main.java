
import javax.swing.JOptionPane;


public class Main {
     public static void main(String[] args){
           
     menu();
     }
     static void menu(){
         int opc = 0, opc1 = 0, opc2 = 0;
        String botones[] = {"1", "2", "3", "4", "Salir"};

        do {
            opc = JOptionPane.showOptionDialog(null, "Elija la opcion:\n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division \n\n", "Menu", JOptionPane.OK_CANCEL_OPTION, JOptionPane.INFORMATION_MESSAGE, null, botones, botones[0]);
            switch(opc){
                case 0:
                    suma();
                    break;
                case 1:
                    rest();
                    break;
                case 2:
                    multi();
                    break;
                case 3:
                    div();
                    break;
                
            }
        }
      while(opc != 4);
         
     }
     
     static void suma(){
         double a,b,c;
         
         try{
             a = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el primer numero"));
             b = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el segundo numero"));
            c = a+b; 
            JOptionPane.showMessageDialog(null, "El resultado de la suma es:  "+ c);
            
         }catch(NumberFormatException e){
             JOptionPane.showMessageDialog(null, "Ingresaste una cadena o un valor que no es un valor valido");
         }
         
         
    }
     
    static void rest(){
         double a,b,c;
         
         try{
             a = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el primer numero"));
             b = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el segundo numero"));
            c = a-b; 
            JOptionPane.showMessageDialog(null, "El resultado de la resta es:  "+ c);
            
         }catch(NumberFormatException e){
             JOptionPane.showMessageDialog(null, "Ingresaste una cadena o un valor que no es un valor valido");
         }
         
     }
     
     static void multi(){
          double a,b,c;
         
         try{
             a = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el primer numero"));
             b = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el segundo numero"));
            c = a*b; 
            JOptionPane.showMessageDialog(null, "El resultado de la muiltiplicacion es:  "+ c);
            
         }catch(NumberFormatException e){
             JOptionPane.showMessageDialog(null, "Ingresaste una cadena o un valor que no es un valor valido");
         }
         
     }
     
     static void div(){
          double a,b,c;
         
         try{
             a = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el primer numero"));
             b = Double.parseDouble(JOptionPane.showInputDialog("Ingresa el segundo numero"));
            c = a/b; 
            JOptionPane.showMessageDialog(null, "El resultado de la division es:  "+ c);
            
         }catch(NumberFormatException e){
             JOptionPane.showMessageDialog(null, "Ingresaste una cadena o un valor que no es un valor valido");
         }
     }
}
