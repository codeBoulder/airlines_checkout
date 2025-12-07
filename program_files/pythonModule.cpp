#include "BookingSystem.h" 
#include <pybind11/pybind11.h>
#include <pybind11/stl.h> 

namespace py = pybind11;
using namespace std;

PYBIND11_MODULE(core_backend, m) {
    m.doc() = "Core C++ Backend for AeroNova";

    py::class_<Airplane>(m, "Airplane")
        .def(py::init<string, int>())
        .def_property_readonly("model", &Airplane::get_airplane_model)
        .def_property_readonly("capacity", &Airplane::get_total_seats);

    py::class_<Flight>(m, "Flight")
        .def_property_readonly("id", &Flight::getID)
        .def_property_readonly("flight_number", &Flight::getFlightNumber)
        .def_property_readonly("origin", &Flight::getOriginCity)
        .def_property_readonly("destination", &Flight::getDestinationCity)
        .def_property_readonly("time", &Flight::getDepartureTime)
        .def_property_readonly("arrival_time", &Flight::getArrivalTime)
        .def_property_readonly("price", &Flight::getBasePrice)
        .def_property_readonly("available_seats", &Flight::getAvailableSeats)
        .def_property_readonly("airplane", &Flight::getAirplane)
        .def("to_dict", &Flight::to_dict);

    py::class_<Passenger>(m, "Passenger")
        .def(py::init<string, string, string, string, int>())
        .def_property_readonly("full_name", &Passenger::get_full_name)
        .def_property_readonly("email", &Passenger::get_email)
        .def_property_readonly("passport", &Passenger::get_passport_num)
        .def_property_readonly("ticket_id", &Passenger::get_ticket_id);

    py::class_<Ticket>(m, "Ticket")
        .def("get_cost", &Ticket::get_cost)
        .def("calculatePrice", &Ticket::calculatePrice);

    py::class_<EconomyTicket, Ticket>(m, "EconomyTicket")
        .def(py::init<int, int, int, int, bool>())
        .def("has_extra_baggage", &EconomyTicket::has_extra_baggage);

    py::class_<BusinessTicket, Ticket>(m, "BusinessTicket")
        .def(py::init<int, int, int, int, bool>())
        .def("get_lounge_access", &BusinessTicket::get_lounge_access);

    py::class_<Employee>(m, "Employee")
        .def("get_name", &Employee::get_name)
        .def("assignDuty", &Employee::assignDuty);

    py::class_<Pilot, Employee>(m, "Pilot")
        .def(py::init<string, string, int, int, int>())
        .def("get_flight_hours", &Pilot::get_flight_hours);

    py::class_<Stewardess, Employee>(m, "Stewardess")
        .def(py::init<string, string, int, int, string>())
        .def("get_language", &Stewardess::get_language);
    
    py::class_<Dispatcher, Employee>(m, "Dispatcher")
         .def(py::init<string, string, int, int, int>())
         .def("get_experience_years", &Dispatcher::get_experience_years);

    py::class_<Cashier, Employee>(m, "Cashier")
         .def(py::init<string, string, int, int, string>())
         .def("get_shift_time", &Cashier::get_shift_time);

    py::class_<BookingSystem>(m, "BookingSystem")
        .def(py::init<>())
        .def("add_flight_from_python", &BookingSystem::add_flight_from_python)
        .def("clear_flights", &BookingSystem::clear_flights)
        .def("get_all_flights_sorted", &BookingSystem::get_all_flights_sorted)
        .def("get_cheapest_flights", &BookingSystem::get_cheapest_flights)
        .def("find_optimal_route", &BookingSystem::find_optimal_route, 
             py::arg("from_city"), py::arg("to_city"), py::arg("minimize_time") = false)
        .def("login_logic", &BookingSystem::login_logic)
        .def("hash_password_cpp", &BookingSystem::hash_password_cpp)
        .def("calculate_ticket_price", &BookingSystem::calculate_ticket_price)
        .def("get_crew_duties", &BookingSystem::get_crew_duties)
        .def("add_passenger_to_hash", &BookingSystem::add_passenger_to_hash)
        .def("find_passenger_by_passport", &BookingSystem::find_passenger_by_passport);
}