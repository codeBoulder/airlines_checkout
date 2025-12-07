#include "BookingSystem.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdint> 
#include <queue>
#include <map>
#include <limits>

using namespace std;

// Hash функції для паролів
std::string HashUtils::to_hex_string(uint32_t hash_value) {
    std::stringstream ss;
    ss << std::hex << std::setw(8) << std::setfill('0') << (hash_value & 0xFFFFFFFF); 
    return ss.str();
}

std::string HashUtils::simple_hash(const std::string& input) {
    uint32_t hash = 5381;
    for (char c : input) {
        hash = ((hash << 5) + hash) + c; 
    }
    return to_hex_string(hash); 
}


// Реалізація базових класів програми
// Airplane
Airplane::Airplane() : airplane_model("Unknown"), total_seats(0) {}
Airplane::Airplane(string model, int seats) 
    : airplane_model(std::move(model)), total_seats(seats) {}

int Airplane::get_total_seats() const { return total_seats; }
string Airplane::get_airplane_model() const { return airplane_model; }

// Passenger
Passenger::Passenger() : first_name(""), surname(""), email(""), passport_num(""), ticket_id(-1) {}

Passenger::Passenger(string f, string s, string e, string p, int t) 
    : first_name(move(f)), surname(move(s)), email(move(e)), passport_num(move(p)), ticket_id(t) {}

string Passenger::get_email() const {return email;}
string Passenger::get_passport_num() const{return passport_num;}
string Passenger::get_full_name() const{return first_name + " " + surname;}
int Passenger::get_ticket_id() const{return ticket_id;}

// Flight
Flight::Flight() 
    : flight_number(""), origin_city(""), destination_city(""), 
      departure_time(""), arrival_time(""), 
      base_price(0.0), ID(0), available_seats(0) 
      {}

Flight::Flight(string num, string orig, string dest, string dep_time, int id, double price, int seats, Airplane plane, string arr_time)
    : flight_number(move(num)), 
      origin_city(move(orig)), 
      destination_city(move(dest)), 
      departure_time(move(dep_time)), 
      arrival_time(move(arr_time)), 
      airplane(plane), 
      base_price(price), 
      ID(id), 
      available_seats(seats) 
      {}

string Flight::getFlightNumber() const { return flight_number; }
string Flight::getOriginCity() const { return origin_city; }
string Flight::getDestinationCity() const { return destination_city; }
string Flight::getDepartureTime() const { return departure_time; }
string Flight::getArrivalTime() const { return arrival_time; }
Airplane Flight::getAirplane() const { return airplane; }
double Flight::getBasePrice() const { return base_price; }
int Flight::getID() const { return ID; }
int Flight::getAvailableSeats() const { return available_seats; }

map<string, string> Flight::to_dict() const {
    return {
        {"flight_number", flight_number},
        {"from_city", origin_city},
        {"to_city", destination_city},
        {"departure_time", departure_time},
        {"base_price", std::to_string(base_price)},
        {"available_seats", std::to_string(available_seats)}
    };
}

// Ticket
Ticket::Ticket(int id, int t_cost, int p, int s) : ID(id), cost(t_cost), place(p), status(s) {}
int Ticket::get_cost() const { return cost; }

EconomyTicket::EconomyTicket(int id, int t_cost, int p, int s, bool eb) : Ticket(id, t_cost, p, s), extra_baggage(eb) {}
bool EconomyTicket::has_extra_baggage() const { return extra_baggage; }
int EconomyTicket::calculatePrice() const { 
    return get_cost(); 
}

BusinessTicket::BusinessTicket(int id, int t_cost, int p, int s, bool la) : Ticket(id, t_cost, p, s), lounge_access(la) {}
bool BusinessTicket::get_lounge_access() const { return lounge_access; }
int BusinessTicket::calculatePrice() const { 
    return static_cast<int>(get_cost() * 1.5); 
}

// Emploee
Employee::Employee(string n, string s, int id, int sal) : name(move(n)), surname(move(s)), ID(id), salary(sal) {}
string Employee::get_name() const { return name; }
string Employee::get_surname() const { return surname; }

Pilot::Pilot(string n, string s, int id, int sal, int fh) : Employee(move(n), move(s), id, sal), flight_hours(fh) {}
int Pilot::get_flight_hours() const { return flight_hours; }
string Pilot::assignDuty() const { return "Flying the aircraft"; }

Stewardess::Stewardess(string n, string s, int id, int sal, string lang) : Employee(move(n), move(s), id, sal), language(move(lang)) {}
string Stewardess::get_language() const { return language; }
string Stewardess::assignDuty() const { return "Serving passengers"; }

Dispatcher::Dispatcher(string n, string s, int id, int sal, int ey) : Employee(move(n), move(s), id, sal), experience_years(ey) {}
int Dispatcher::get_experience_years() const { return experience_years; }
string Dispatcher::assignDuty() const { return "Coordinating flight schedules"; }

Cashier::Cashier(string n, string s, int id, int sal, string st) : Employee(move(n), move(s), id, sal), shift_time(move(st)) {}
string Cashier::get_shift_time() const { return shift_time; }
string Cashier::assignDuty() const { return "Selling tickets"; }


// BookingSystem (основиний клас з реалізацією методів)
BookingSystem::BookingSystem() {}

// Хешування введеного паролю
string BookingSystem::hash_password_cpp(const string& password) {
    return HashUtils::simple_hash(password);
}

// Логіка входу користувача у акаунт
string BookingSystem::login_logic(const string& entered_password, const string& stored_hash) {
    string hashed_input = HashUtils::simple_hash(entered_password);
    return (hashed_input == stored_hash) ? "success" : "wrong_password";
}

void BookingSystem::clear_flights() {
    flights.clear();
}

// Формування списку рейсів переданих з Python
void BookingSystem::add_flight_from_python(int id, string num, string origin, string dest, double price, int seats, string dep_time) {
    Airplane plane("Boeing 737", seats); 
    string default_arrival = "00:00"; 
    flights.emplace_back(num, origin, dest, dep_time, id, price, seats, plane, default_arrival);
}

// QuickSort
int BookingSystem::partition(int low, int high) {
    string pivot = flights[high].getDepartureTime(); 
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++) {
        if (flights[j].getDepartureTime() < pivot) {
            i++;
            swap(flights[i], flights[j]);
        }
    }
    swap(flights[i + 1], flights[high]);
    return (i + 1);
}

void BookingSystem::quickSortRecursive(int low, int high) {
    if (low < high) {
        int pi = partition(low, high);
        quickSortRecursive(low, pi - 1);
        quickSortRecursive(pi + 1, high);
    }
}

void BookingSystem::sortFlightsByTime() {
    if (!flights.empty()) {
        quickSortRecursive(0, flights.size() - 1);
    }
}

// Жадібний алгоритм для пошуку найдешевших рейсів
vector<Flight> BookingSystem::getCheapestFlightsGreedy(int count) {
    vector<Flight> result;
    if (flights.empty()) return result;
    vector<Flight> temp = flights; 
    
    for (int i = 0; i < count && !temp.empty(); ++i) {
        int minIndex = 0;
        for (size_t j = 1; j < temp.size(); ++j) { 
            if (temp[j].getBasePrice() < temp[minIndex].getBasePrice()) {
                minIndex = j;
            }
        }
        result.push_back(temp[minIndex]);
        temp.erase(temp.begin() + minIndex);
    }
    return result;
}

// Функції-обгортки для Python
vector<Flight> BookingSystem::get_all_flights_sorted() {
    sortFlightsByTime(); 
    return flights;
}

vector<Flight> BookingSystem::get_cheapest_flights(int limit) {
    return getCheapestFlightsGreedy(limit);
}

// Алгоритм Дейкстри для пошуку оптимального маршруту
int get_duration_minutes(const string& dep, const string& arr) {
    try {
        int h1 = stoi(dep.substr(0, 2));
        int m1 = stoi(dep.substr(3, 2));
        int start = h1 * 60 + m1;

        int h2 = stoi(arr.substr(0, 2));
        int m2 = stoi(arr.substr(3, 2));
        int end = h2 * 60 + m2;

        if (end < start) return (24 * 60 - start) + end; 
        return end - start;
    } catch (...) {
        return 60; 
    }
}

vector<Flight> BookingSystem::find_optimal_route(string from_city, string to_city, bool minimize_time) {
    map<string, vector<Flight>> adj;
    for (const auto& f : flights) {
        adj[f.getOriginCity()].push_back(f);
    }

    map<string, double> min_cost;      
    map<string, Flight> parent_flight; 
    map<string, string> previous_city; 

    priority_queue<pair<double, string>, vector<pair<double, string>>, greater<pair<double, string>>> pq;

    min_cost[from_city] = 0.0;
    pq.push({0.0, from_city});

    while (!pq.empty()) {
        double current_cost = pq.top().first;
        string u = pq.top().second; 
        pq.pop();

        if (min_cost.find(u) != min_cost.end() && current_cost > min_cost[u]) {
            continue;
        }

        if (u == to_city) break;

        if (adj.find(u) != adj.end()) {
            for (const auto& flight : adj[u]) {
                string v = flight.getDestinationCity();
                
                double weight;
                if (minimize_time) {
                    weight = (double)get_duration_minutes(flight.getDepartureTime(), flight.getArrivalTime());
                } else {
                    weight = flight.getBasePrice();
                }

                if (min_cost.find(v) == min_cost.end() || min_cost[u] + weight < min_cost[v]) {
                    min_cost[v] = min_cost[u] + weight;
                    parent_flight[v] = flight; 
                    previous_city[v] = u;      
                    pq.push({min_cost[v], v});
                }
            }
        }
    }

    vector<Flight> route;
    if (min_cost.find(to_city) == min_cost.end()) {
        return route; 
    }

    string current = to_city;
    while (current != from_city) {
        route.push_back(parent_flight[current]);
        current = previous_city[current];
    }

    reverse(route.begin(), route.end());
    return route;
}

// Підрахунок вартості квитка в залежності від класу 
double BookingSystem::calculate_ticket_price(double base_price, int type) {
    Ticket* ticket;
    if (type == 1) {
        ticket = new BusinessTicket(0, (int)base_price, 0, 0, true);
    } else {
        ticket = new EconomyTicket(0, (int)base_price, 0, 0, false);
    }
    
    double final_price = ticket->calculatePrice();
    delete ticket; 
    return final_price;
}

// Отримання екіпажу літака
vector<string> BookingSystem::get_crew_duties(vector<string> names, vector<string> surnames, vector<string> roles) {
    vector<string> result_duties;
    
    for (size_t i = 0; i < names.size(); ++i) {
        Employee* emp = nullptr;
        string role = roles[i];

        if (role == "Pilot" || role == "Captain" || role == "First Officer") {
            emp = new Pilot(names[i], surnames[i], 0, 0, 0); 
        } else if (role == "Stewardess" || role == "Flight Attendant") {
            emp = new Stewardess(names[i], surnames[i], 0, 0, "UA");
        } else {
            emp = new Cashier(names[i], surnames[i], 0, 0, "Day"); 
        }

        if (emp) {
            string info = emp->get_name() + " " + emp->get_surname() + " (" + role + "): " + emp->assignDuty();
            result_duties.push_back(info);
            delete emp;
        }
    }
    return result_duties;
}

// Хеш-таблия для отримання даних про користувача, а ключем є паспортні дані користувача
void BookingSystem::add_passenger_to_hash(string fname, string sname, string mail, string passport, int ticket_id) {
    Passenger p(fname, sname, mail, passport, ticket_id);
    passengers_hash_table[passport] = p;
}

Passenger BookingSystem::find_passenger_by_passport(string passport) {
    if (passengers_hash_table.find(passport) != passengers_hash_table.end()) {
        return passengers_hash_table[passport];
    }
    return Passenger("Not Found", "", "", "", -1);
}