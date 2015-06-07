/*
  MATH491: Research
  Computational Number Theory Group: Stephen Caps, Sarah Sahibzada, Taylor Wilson
  Simple fibonacci generator; generates successive pairs of fibonacci numbers and exports to csv or txt
*/

import java.math.BigInteger;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.lang.String;
import java.lang.StringBuilder;

public class fibonacciGenerator {
	int numPairs;
	
	public fibonacciGenerator(int pairs) {
		
		this.numPairs = pairs;
	}
	public fibonacciGenerator() {
		this.numPairs = 10000; //default number of pairs
	}
	public static void generateTextFile(int length) throws IOException {
		FileWriter toTxtFile = new FileWriter("FibonacciPairs.txt");
		try {
			BigInteger seed1 = BigInteger.ONE;
			BigInteger seed2 = BigInteger.ONE;
			BigInteger next = BigInteger.ONE;
			toTxtFile.append("1\t\t,\t\t1\n"); //hard coded 
			while (length != 0) {
				//simple iterative fibonacci
				toTxtFile.append((CharSequence)next.toString());
				toTxtFile.append("\t\t,\t\t"); //for readability
				next = seed1.add(seed2);
				seed1 = seed2;
				seed2 = next;
				toTxtFile.append((CharSequence)next.toString());	
				toTxtFile.append('\n');
				length -= 1;
			}		
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			toTxtFile.flush();
			toTxtFile.close();
			System.out.println("Find your data in FibonacciPairs.txt");
		}
	}
	
	public static void generateCSVFile(int length) throws IOException {
		FileWriter toTxtFile = new FileWriter("FibonacciPairs.csv");
		try {
			BigInteger seed1 = BigInteger.ONE;
			BigInteger seed2 = BigInteger.ONE;
			BigInteger next = BigInteger.ONE;
			toTxtFile.append("1\t\t,\t\t1\n"); //hard coded
			while (length != 0) {
				//simple iterative fibonacci
				toTxtFile.append((CharSequence)next.toString());
				toTxtFile.append(','); //for readability
				next = seed1.add(seed2);
				seed1 = seed2;
				seed2 = next;
				toTxtFile.append((CharSequence)next.toString());
				toTxtFile.append('\n');	
				length -= 1;
			}		
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			toTxtFile.flush();
			toTxtFile.close();
			System.out.println("Find your data in FibonacciPairs.csv");
		}
	}
	
	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		int userChoice;
		int numToGen;
		System.out.println("This program will generate pairs of successive Fibonacci numbers.");
		System.out.println("[1] As .txt file");
		System.out.println("[2] As .csv file");
		userChoice = input.nextInt();
		switch(userChoice) {
		case 1:
			System.out.println("Enter the number of pairs you want to generate.");
			numToGen = input.nextInt();
			generateTextFile(numToGen);
			break;
		case 2:
			System.out.println("Enter the number of pairs you want to generate.");
			numToGen = input.nextInt();
			generateCSVFile(numToGen);
			break;
		default:
			System.out.println("Bad input. Exiting.");
			break;
		}
		
	}
	
	
	
}
