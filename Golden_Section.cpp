#include<iostream>
#include<math.h>

#define ro (3-sqrt(5))/2

const double f_x(double x){

	const double y = pow(x, 4) - 14 * pow(x, 3) + 60 * pow(x,2) - 70 * x + 10;

	return y;

}

void golden_method(double tail,double head, double rng = 1) {

	int number_of_itr = ceil(log(rng / 2) / log(1 - ro));
	double a_new = tail + ro * (head - tail);
	double b_new = tail + (1 - ro)*(head - tail);
	std::cout <<"Initial searching range is : "<< "[a , b] = [" << tail << "," << head << "]\n\n";


	for (int i = 0; i < number_of_itr; i++) {

		double f_anew = f_x(a_new);
		double f_bnew = f_x(b_new);

		if (f_anew < f_bnew) {

			tail = tail;
			head = b_new;

			b_new = a_new;
			a_new = tail + ro * (head - tail);
		}
		else {
			head = head;
			tail = a_new;

			a_new = b_new;
			b_new = tail + (1 - ro)*(head - tail);
		}

	    std::cout <<" Iteration "<< i+1 <<"\n [a , b] = ["<< tail << "," << head<<"]\n";
		std::cout << " b - a = " << head - tail<<"\n\n"; 
		
	}
	std::cout << "The minimum point is between the range of [a , b] = [" << tail << "," << head << "]";
}



int main() {
	
	golden_method(0.0, 2.0, 0.3);
    std::getchar();
	return 0; 

}
