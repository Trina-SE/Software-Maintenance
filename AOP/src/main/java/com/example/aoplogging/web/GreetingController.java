package com.example.aoplogging.web;

import com.example.aoplogging.service.GreetingService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    private final GreetingService greetingService;

    public GreetingController(GreetingService greetingService) {
        this.greetingService = greetingService;
    }

    @GetMapping("/greet")
    public ResponseEntity<String> greet(@RequestParam(defaultValue = "Baeldung") String name) {
        return ResponseEntity.ok(greetingService.greet(name));
    }

    @GetMapping("/")
    public ResponseEntity<String> root() {
        // Provide a simple root response so browsing to `/` doesn't return Whitelabel 404
        return ResponseEntity.ok(greetingService.greet("World"));
    }
}

