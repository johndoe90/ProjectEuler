public class Main {	
	public static void main(String[] args) {
		Set<BigInteger> results = new HashSet<>();
		
		for ( int a = 2; a <= 100; a++ ) 
			for ( int b = 2; b <= 100; b++ ) 
				results.add(BigInteger.valueOf(a).pow(b));
		
		System.out.println(results.size());
	}
}
