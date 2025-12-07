#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <cstdint>
#include <sstream>
#include <iomanip>
#include <queue>

using namespace std;

// Hash утиліти
class HashUtils {
public:
    static std::string simple_hash(const std::string& input);
    static std::string to_hex_string(uint32_t hash_value);
};

// Базові класи програми
class Airplane {
private:
    string airplane_model;
    int total_seats;

public:
    Airplane(); 
    Airplane(string model, int seats);
    
    int get_total_seats() const;
    string get_airplane_model() const;
};

class Flight {
private:
    string flight_number;
    string origin_city;
    string destination_city;
    string departure_time;
    string arrival_time;
    Airplane airplane; 
    double base_price;
    int ID;            
    int available_seats;

public:
    Flight(); 
    Flight(string num, string orig, string dest, string dep_time, int id, double price, int seats, Airplane plane, string arr_time);

    string getFlightNumber() const;
    string getOriginCity() const;
    string getDestinationCity() const;
    string getDepartureTime() const;
    string getArrivalTime() const;
    Airplane getAirplane() const;
    double getBasePrice() const;
    int getID() const;
    int getAvailableSeats() const;

    map<string, string> to_dict() const;
};

class Ticket {
private:
    int ID;
    int cost;
    int place;
    int status; 

public:
    Ticket(int id, int t_cost, int p, int s);
    virtual ~Ticket() = default;
    
    virtual int calculatePrice() const = 0; 
    
    int get_cost() const;
};

class EconomyTicket : public Ticket {
private:
    bool extra_baggage;
public:
    EconomyTicket(int id, int t_cost, int p, int s, bool eb);
    bool has_extra_baggage() const;
    int calculatePrice() const override;
};

class BusinessTicket : public Ticket {
private:
    bool lounge_access;
public:
    BusinessTicket(int id, int t_cost, int p, int s, bool la);
    bool get_lounge_access() const;
    int calculatePrice() const override;
};

class Employee {
protected:
    string name;
    string surname;
    int ID;
    int salary;

public:
    Employee(string n, string s, int id, int sal);
    virtual ~Employee() = default;
    
    virtual string assignDuty() const = 0; 
    
    string get_name() const;
    string get_surname() const;
};

class Pilot : public Employee {
private:
    int flight_hours;
public:
    Pilot(string n, string s, int id, int sal, int fh);
    int get_flight_hours() const;
    string assignDuty() const override;
};

class Stewardess : public Employee {
private:
    string language;
public:
    Stewardess(string n, string s, int id, int sal, string lang);
    string get_language() const;
    string assignDuty() const override;
};

class Dispatcher : public Employee {
private:
    int experience_years;
public:
    Dispatcher(string n, string s, int id, int sal, int ey);
    int get_experience_years() const;
    string assignDuty() const override;
};

class Cashier : public Employee {
private:
    string shift_time;
public:
    Cashier(string n, string s, int id, int sal, string st);
    string get_shift_time() const;
    string assignDuty() const override;
};

class Passenger {
private:
    string first_name;
    string surname;
    string email;
    string passport_num;
    int ticket_id;

public:
    Passenger();
    Passenger(string fname, string sname, string mail, string pnum, int t);
    
    string get_email() const;
    string get_passport_num() const;
    string get_full_name() const;
    int get_ticket_id() const;
};

// Головна система бронювання
class BookingSystem {
private:
    // Дані про рейси
    vector<Flight> flights;

    // Хеш-таблиця для пасажирів
    unordered_map<string, Passenger> passengers_hash_table;

    int partition(int low, int high);
    void quickSortRecursive(int low, int high);

public:
    BookingSystem(); 

    // Робота з даними
    void clear_flights(); 
    void add_flight_from_python(int id, string num, string origin, string dest, double price, int seats, string dep_time); 

    // Алгоритми
    void sortFlightsByTime(); 
    vector<Flight> getCheapestFlightsGreedy(int count); 
    vector<Flight> find_optimal_route(string from_city, string to_city, bool minimize_time);

    // Обгортки для Python
    vector<Flight> get_all_flights_sorted(); 
    vector<Flight> get_cheapest_flights(int limit); 

    // Авторизація
    string hash_password_cpp(const string& password); 
    string login_logic(const string& entered_password, const string& stored_hash); 

    // Поліморфізм (Нові методи)
    double calculate_ticket_price(double base_price, int type);
    vector<string> get_crew_duties(vector<string> names, vector<string> surnames, vector<string> roles);

    // Хеш-таблиця для пасажирів
    void add_passenger_to_hash(string fname, string sname, string mail, string passport, int ticket_id);
    Passenger find_passenger_by_passport(string passport);

};