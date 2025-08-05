
class Student {
    String name;
    int age;
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}
class GraduateStudent extends Student {
    String thesisTitle; 
    GraduateStudent(String name, int age, String thesisTitle) {
        super(name, age);
        this.thesisTitle = thesisTitle;
    }
    @Override
    void displayDetails() {
        super.displayDetails();
        System.out.println("Thesis Title: " + thesisTitle);
    }
}
public class Main {
    public static void main(String[] args) {
        GraduateStudent gradStudent = new GraduateStudent("minka easmin", 22, "anything");
        gradStudent.displayDetails();
    }
}
