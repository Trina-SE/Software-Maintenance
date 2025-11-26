package com.example.aoplogging;

import static org.assertj.core.api.Assertions.assertThat;

import com.example.aoplogging.service.GreetingService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class GreetingServiceTests {

    @Autowired
    private GreetingService greetingService;

    @Test
    void givenName_whenGreet_thenReturnGreeting() {
        String result = greetingService.greet("Baeldung");
        assertThat(result).isEqualTo("Hello Baeldung");
    }
}

