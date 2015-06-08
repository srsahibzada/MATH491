/*
	MATH 491 Computational Number Theory group: Stephen Capps, Sarah Sahibzada, Taylor Wilson
	Code by Sarah Sahibzada
	Performs Extended Euclidean Algorithm on a user-specified amount of random numbers of arbitrary length
	and writes them to a CSV.
*/


import java.math.BigInteger;
import java.math.BigDecimal;
import java.lang.String;
import java.lang.Thread;
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.math.MathContext;


public class testEEA {
	public static ArrayList<testEEA> EEAList = new ArrayList<testEEA>();
	public static final String CSVMODE = ".csv";
	private static final String TXTMODE = ".txt";
	String mode;
	int digits;
	int pairs;
	private BigInteger firstArg;
	private BigInteger secondArg;
	private BigDecimal ratio;
	private BigInteger numIterations;
	private BigInteger finalBezoutCoeff1;
	private BigInteger finalBezoutCoeff2;
	private BigInteger gcd;
	private ArrayList<BigInteger> firstCoeffs = new ArrayList<BigInteger>();
	private ArrayList<BigInteger> secondCoeffs = new ArrayList<BigInteger>();
	//constants
	public static final int LESS = -1;
	public static final int EQUALS = 0;
	public static final int GREATER = 1;
	public static final char COMMA = ',';
	public static final char DELIM = ' ';
	public static final char NEWLINE = '\n';
	public static final char LEFTPAREN = '(';
	public static final char RIGHTPAREN = ')';
	public static final String FIRSTARG = "A";
	public static final String SECONDARG = "B";
	public static final String RATIO = "Ratio A/B";
	public static final String BEZOUT1 = "First Bezout";
	public static final String BEZOUT2 = "Second Bezout";
	public static final String GCD = "GCD";
	public static final String NUM = "# Iterations";
	public static final int maxNumDecimalPlaces = 10;
	

	testEEA(BigInteger a, BigInteger b) {
	if (a.compareTo(b) == LESS) {
		BigInteger temp = b;
		b = a;
		a = temp;
	}
		this.firstArg = a;
		this.secondArg = b;
	}
	
		testEEA(BigInteger a, BigInteger b, BigDecimal r, BigInteger n, BigInteger fbc1, BigInteger fbc2, BigInteger gcd, ArrayList<BigInteger> first, ArrayList<BigInteger> second) {
		if (a.compareTo(b) == LESS) {
			BigInteger temp = b;
			b = a;
			a = temp;
		}
			this.firstArg = a;
			this.secondArg = b;
			this.ratio = r;
			this.numIterations = n;
			this.finalBezoutCoeff1 = fbc1;
			this.finalBezoutCoeff2 = fbc2;
			this.gcd = gcd;
			this.firstCoeffs = first;
			this.secondCoeffs = second;
		}
	testEEA() {
		//null
	}
	
	public BigInteger getGCD() {
		return this.gcd;
	}
	public BigDecimal getRatio() {
		return this.ratio;
	}
	public BigInteger getFirstArg() {
		return this.firstArg;
	}
	public BigInteger getSecondArg() {
		return this.secondArg;
	}
	public BigInteger getnumIterations() {
		return this.numIterations;
	}
	public BigInteger getFirstBezout() {
		return this.finalBezoutCoeff1;
	}
	public BigInteger getSecondBezout() {
		return this.finalBezoutCoeff2;
	}
	
	public void addToList(boolean which, BigInteger coeff) {
		if (which) {
			firstCoeffs.add(coeff);
		}
		else {
			secondCoeffs.add(coeff);
		}
	}
	
	public String getFieldString(String field) {
		if (field.equals(FIRSTARG)) {
			return firstArg.toString();
		}
		else if (field.equals(SECONDARG)) {
			return secondArg.toString();
		}
		else if (field.equals(RATIO)) {
			return ratio.toString();
		}
		else if (field.equals(BEZOUT1)) {
			return finalBezoutCoeff1.toString();
		}
		else if (field.equals(BEZOUT2)) {
			return finalBezoutCoeff2.toString();
		}
		else if (field.equals(NUM)) {
			return numIterations.toString();
		}
		else if (field.equals(GCD)) {
			return gcd.toString();
		}
		else {
			return "error";
		}
	}
	@Override
	public String toString() {
	String toReturn = new String();
		toReturn += ("A: " + this.getFieldString(FIRSTARG));
		toReturn += ("B: " + this.getFieldString(SECONDARG));
		toReturn += ("# Iter" + this.getFieldString(NUM));
		toReturn += ("Bezout 1:" + this.getFieldString(BEZOUT1));
		toReturn += ("Bezout 2:" + this.getFieldString(BEZOUT2));
		toReturn += ("GCD: " + this.getFieldString(GCD));
		toReturn += ("Ratio: "+this.getFieldString(RATIO));
		toReturn += NEWLINE;
		return toReturn;
	}
	public static BigDecimal computeRatio(BigInteger a, BigInteger b) {
		MathContext roundingError = new MathContext(maxNumDecimalPlaces); //at most 10 decimal places
		if (a.compareTo(b) == LESS) {
			BigInteger temp = b;
			b = a;
			a = temp;
		}
		BigDecimal decA = new BigDecimal(a);
		BigDecimal decB = new BigDecimal(b);
		BigDecimal ratio = decA.divide(decB, roundingError);
		return ratio;
	}		
	public static testEEA extended_Euclidean(BigInteger _a, BigInteger _b) {
		if (_a.compareTo(_b) == LESS) {
			BigInteger temp = _b;
			_b = _a;
			_a = temp;
	}
	//testEEA(BigInteger a, BigInteger b, BigDecimal r, BigInteger n, BigInteger fbc1, BigInteger fbc2, BigInteger gcd, ArrayList<BigInteger> first, ArrayList<BigInteger> second) {

		ArrayList<BigInteger> futureFirst = new ArrayList<BigInteger>();
		ArrayList<BigInteger> futureSecond = new ArrayList<BigInteger>();
		BigInteger old_r = _a;
		BigInteger r = _b;
		BigInteger s = new BigInteger("0");
		BigInteger t = new BigInteger("1");
		BigInteger old_s = new BigInteger("1");
		BigInteger old_t = new BigInteger("0");
		BigInteger temp;
		BigInteger numIterations = BigInteger.ZERO;
		//wiki algorithm for extended euclidean algorithm
		while(!r.equals(BigInteger.ZERO)) {
			futureFirst.add(old_s);
			futureSecond.add(old_t);
			numIterations = numIterations.add(BigInteger.ONE);
			BigInteger quotient = old_r.divide(r);
			temp = old_r;
			old_r = r;
			r = temp.subtract(quotient.multiply(r));
			temp = old_s;
			old_s = s;
			s = temp.subtract(quotient.multiply(s));
			temp = old_t;
			old_t = t;
			t = temp.subtract(quotient.multiply(t));
		}
			futureFirst.add(old_s);
			futureSecond.add(old_t);


		testEEA toReturn = new testEEA(_a,_b,computeRatio(_a,_b), numIterations, old_s, old_t, old_r, futureFirst, futureSecond);
		return toReturn;
		}
	//http://stackoverflow.com/questions/3709521/how-do-i-generate-a-random-n-digit-integer-in-java-using-the-biginteger-class
	public static BigInteger genRandom(int numDigits, Random r) {
	    final char[] ch = new char[numDigits];
		for(int i = 0; i < numDigits; i++) {
        ch[i] =
            (char) ('0' + (i == 0 ? r.nextInt(9) + 1 : r.nextInt(10)));
    }
	//System.out.println(new BigInteger(new String(ch)).toString()); //uncomment to verify
    return new BigInteger(new String(ch));
	}
	
	public static void addToFile(String destinationFile, String mode) throws IOException {
	FileWriter toFile = new FileWriter(destinationFile + mode);
		try{
			toFile.append(FIRSTARG);
			toFile.append(COMMA);
			toFile.append(SECONDARG);
			toFile.append(COMMA);
			toFile.append(RATIO);
			toFile.append(COMMA);
			toFile.append(GCD);
			toFile.append(COMMA);
			toFile.append(NUM);
			toFile.append(COMMA);
			toFile.append(BEZOUT1);
			toFile.append(COMMA);
			toFile.append(BEZOUT2);
			toFile.append(NEWLINE);
			for (testEEA t: EEAList) {
				toFile.append(t.getFieldString(FIRSTARG));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(SECONDARG));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(RATIO));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(GCD));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(NUM));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(BEZOUT1));
				toFile.append(COMMA);
				toFile.append(t.getFieldString(BEZOUT2));			
				toFile.append(NEWLINE);
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			toFile.flush();
			toFile.close();
			System.out.println("All input written to file " + destinationFile + mode );
		}
	}
	public static void writeCoeffsToFile(String fileName) throws IOException {
		FileWriter coeffsFiles = new FileWriter(fileName);
		try {
			for (testEEA t : EEAList) {
				coeffsFiles.append(LEFTPAREN);
				coeffsFiles.append(t.getFirstArg().toString());
				coeffsFiles.append(DELIM);
				coeffsFiles.append(t.getSecondArg().toString());
				coeffsFiles.append(RIGHTPAREN);
				coeffsFiles.append(COMMA);
				for(int i = 0; i < t.firstCoeffs.size(); i++) {
					coeffsFiles.append(LEFTPAREN);
				coeffsFiles.append(t.firstCoeffs.get(i).toString());
				coeffsFiles.append(DELIM);
				coeffsFiles.append(t.secondCoeffs.get(i).toString());
				coeffsFiles.append(RIGHTPAREN);
				coeffsFiles.append(COMMA);
				}
				
				coeffsFiles.append(NEWLINE);
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		finally {
			coeffsFiles.flush();
			coeffsFiles.close();
		}
	}
	//for testing and debugging
	public static void printEEAList() {
		for (testEEA t : EEAList) {
			System.out.println(t); 
		}
	}
	
	//generates the list
	public static void EEAWriter(int numDigits, int numPairs) {
		for (int i = 0; i < numPairs; i++) {
		Random r1 = new Random();
		Random r2 = new Random();
		testEEA EEAobj = extended_Euclidean(genRandom(numDigits,r1), genRandom(numDigits,r2));
		EEAList.add(EEAobj);
		}	
	}
	
	//for testing purposes
	public static boolean testEEAList() {
		int i = 0;
		for (testEEA t : EEAList) {
			System.out.println(t);
			if (((t.getFirstArg().multiply(t.getFirstBezout())).add(t.getSecondArg().multiply(t.getSecondBezout()))).equals(t.getGCD())) {
				i += 1;
			}
		}
		return (i == EEAList.size());
	}
	public static void main(String[] args) throws IOException {
		Scanner input = new Scanner(System.in);
		int userChoice;
		int numToGen;
		int numDigits;
		String storeCoeffs;
		String fileName;
		System.out.println("This program will generate data on the Euclidean algorithm using random numbers of a user-specified length. Do you want this as:");
		System.out.println("[1] A .txt file");
		System.out.println("[2] A .csv file"); 
		userChoice = input.nextInt();
		switch(userChoice) {
			case 1:
				System.out.println("How many pairs do you wish to generate?");
				numToGen = input.nextInt();
				System.out.println("How many digits long do you want the numbers to be?");
				numDigits = input.nextInt();
				System.out.println("Name the file (do not include file extension).");
				fileName = input.next();
				EEAWriter(numDigits,numToGen);
				addToFile(fileName,TXTMODE);
				writeCoeffsToFile(fileName+"_coefficient_list"+CSVMODE);
				//System.out.println("EEAList correct values: " + testEEAList());//uncomment to verify list				
				break;
			case 2:
				System.out.println("How many pairs do you wish to generate?");
				numToGen = input.nextInt();
				System.out.println("How many digits long do you want the numbers to be?");
				numDigits = input.nextInt();
				System.out.println("Name the file (do not include file extension).");
				fileName = input.next();
				EEAWriter(numDigits,numToGen);
				addToFile(fileName,CSVMODE);
				writeCoeffsToFile(fileName+"_coefficient_list"+CSVMODE);
				//System.out.println("EEAList correct values: " + testEEAList());//uncomment to verify list
				break;
			default:
				System.out.println("Bad input, exiting now");
				break;
		}
	}

	
}

class main {
	testEEA t = new testEEA();
}



