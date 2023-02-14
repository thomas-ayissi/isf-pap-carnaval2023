package tp01;

import java.util.Random;
import java.util.Scanner;

public class Jeu {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		// create instance of Random class
		Random rand = new Random();
		int secret = rand.nextInt(100) + 1;
	
		boolean trouve = false;
		do {
			System.out.println("Entrez un nombre entre 1 et 100");
			int nbr = scan.nextInt();

			if (nbr < secret)
				System.out.println("Trop petit");
			else if (nbr > secret)
				System.out.println("Trop grand");
			else {
				System.out.println("Super tu l'as trouvé");
				trouve = true;
			}
		} while (!trouve);
		System.out.println("Fin");
		scan.close();
	}

}
