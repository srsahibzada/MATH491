/*
	Sarah Sahibzada, Taylor Wilson and Stephen Capps
	Math 491: Research
	The purpose of this program is to calculate the greatest common divisor (GCD) of two large numbers
	using the extended euclidean algorithm and monitor the number of iterations taken to completion.
	Relevant data collected are:
		-for a and b, if a and b are even or odd
		-maximum bound of iterations to completion of EEA
		-actual number of iterations to complete EEA
	This program will run 10 threads to perform calculations and write to the CSV. This allows 10 calculations
	to be performed at once.

*/
import java.math.BigInteger;
import java.lang.String;
import java.lang.Thread;
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.StringBuilder;
import java.io.IOException;
//global biginteger function

public class EuclideanAlgorithm implements Runnable {
	//variables to be monitored
	BigInteger a;
	BigInteger b;
	BigInteger numIterations = new BigInteger("0");
	BigInteger gcd;
	boolean aParity;
	boolean bParity;
	int numDigits;

	//stuff for csv file
	String myCSVPath;

	//useful constants
	public static final int LESS = -1;
	public static final int EQUALS = 0;
	public static final int GREATER = 1;
	public static final boolean ODD = true; //odd mod 2 is 1
	public static final boolean EVEN = false; //even mod 2 is 0

	//with two preset 
	public EuclideanAlgorithm(BigInteger firstArg, BigInteger secondArg) {
		if (firstArg.compareTo(secondArg).equals(LESS)) {
			BigInteger temp = new BigInteger("0");
			temp = secondArg;
			secondArg = firstArg;
			firstArg = temp;
			this.a = firstArg;
			this.b = secondArg;
		}
		else {
			//set a and b
			this.a = firstArg;
			this.b = secondArg;
		}
	}
	public BigInteger genRandom(int numDigits) {
		Random r = new Random();
		StringBuilder bitString = new StringBuilder(numDigits);
		for (int i = 0; i < numDigits; i++) {
			bitString.append((char)r.nextInt(10));
		}
		String finalBitString = bitString.toString();
		BigInteger rand = new BigInteger(finalBitString);
	}

	private void setCSVPath(String path) {
		this.myCSVPath = path;
	}
	private void calcAParity() {
		this.aParity = a.mod(new BigInteger("2"));
	}
	private void calcBParity() {
		this.bParity = b.mod(BigInteger.TWO);
	}

	//note that this needs to be locked as appropriate
	public void writeToCSV(String destinationFile) {
		FileWriter toCSV = new FileWriter(destinationFile);
		toCSV.append(a.toString());
		toCSV.append(',');
		toCSV.append(b.toString());


		toCSV.flush();
		toCSV.close();

	}

	public static BigInteger[] extended_Euclidean(final BigInteger _a, final BigInteger _b) {
		BigInteger[] to_return = new BigInteger[4];
		BigInteger old_r = _a;
		BigInteger r = _b;
		BigInteger s = new BigInteger("0");
		BigInteger t = new BigInteger("1");
		BigInteger old_s = new BigInteger("1");
		BigInteger old_t = new BigInteger("0");
		BigInteger numIterations = 0;
		while(!r.equals(BigInteger.ZERO)) {
			BigInteger quotient = old_r.divide(r);
			BigInteger buff = r;
			r = old_r.subtract(quotient.multiply(buff));
			old_r = buff;
			buff = s;
			s = old_s.subtract(quotient.multiply(buff));
			old_s = buff;
			buff = t;
			t = old_t.subtract(quotient.multiply(buff));
			old_t = buff;
			numIterations += 1;
		}

		to_return[0] = old_s;
		to_return[1] = old_t;
		to_return[2] = old_r;
		to_return[3] = numIterations;
		return to_return;
	}


	//private setParity()
	@Override
	public void run() {


	}

}