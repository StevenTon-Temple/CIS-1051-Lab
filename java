package com.example.lab;

public class Draw {
    public static final int SIZE = 1;
    public static final int HEIGHT1 = 8;
    public static final int HEIGHT2 = 3;
    public static void main(String[] args) {
        slug();
        POINTINGFINGER();
        SOMETHING();
    }
    public static void slug() {
        for (int i = SIZE; i <= HEIGHT1; i++)
            System.out.print("|-----");
            System.out.print("\n");
                for (int i = SIZE; i < HEIGHT1-2; i++)
                    System.out.println("|-----" + "|" +"  []  []   []      []    []      []     |");
                    for (int i = SIZE; i <= HEIGHT1; i++)
                        System.out.print("|-----");
    }
    public static void POINTINGFINGER() {
        System.out.println("\n");
        for (int i = SIZE; i <=HEIGHT2; i++)
            System.out.print("|---");
            System.out.print("()");
            for (int i = SIZE; i <=HEIGHT2+2; i++)
                System.out.println("|---------"+ ")");
                }
    public static void SOMETHING(){
        System.out.println("\n");
        for (int i = SIZE; i <=HEIGHT2; i++)
            System.out.print("|---");
            System.out.print("()");
                for (int i = SIZE; i <=HEIGHT2+2; i++)
                System.out.println("|---------"+ ")");
                    for (int i = SIZE; i <=HEIGHT2-1; i++)
                    System.out.print("--------"+ ")");
    }
    }
    ///Didn't realize but they look like sizeways buildings///
