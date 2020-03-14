import java.util.*;

class AreaOfCircle {
    private float radius = 0.0f;
    private float area = 0.0f;
    private float perimeter = 0.0f;

    // function to read radius
    public void readRadius() {
        // Scanner class - to read value from keyboard
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter radius:");
        radius = sc.nextFloat(); // to read float value from keyboard
    }

    // funtction to calculate area
    // return value - will return calculated area
    public float getArea() {
        area = Math.PI * radius * radius;
        return area;
    }

    // funtction to calculate perimeter
    // return value - will return calculated perimeter
    public float getPerimeter() {
        perimeter = 2 * Math.PI * radius;
        return perimeter;
    }
}

public class find_area_and_perimeter_of_a_circle {
    public static void main(String[] s) {
        AreaOfCircle area = new AreaOfCircle();

        area.readRadius();
        System.out.println("Area of circle:" + area.getArea());
        System.out.println("Perimeter of circle:" + area.getPerimeter());
    }
}
