package com.example.aoplogging.logging;

import java.util.Arrays;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    private static final Logger logger = LoggerFactory.getLogger(LoggingAspect.class);

    @Pointcut("execution(public * com.example.aoplogging..*(..))")
    private void applicationPackagePointcut() {
        // pointcut signature
    }

    @Around("applicationPackagePointcut()")
    public Object logAround(ProceedingJoinPoint joinPoint) throws Throwable {
        var args = Arrays.toString(joinPoint.getArgs());
        var methodName = joinPoint.getSignature().toShortString();
        logger.info(">> {} - args={}", methodName, args);
        try {
            Object result = joinPoint.proceed();
            logger.info("<< {} - result={}", methodName, result);
            return result;
        } catch (Throwable throwable) {
            logger.error("!! {} - exception={}", methodName, throwable.getMessage());
            throw throwable;
        }
    }

    @Before("applicationPackagePointcut()")
    public void logBefore(JoinPoint joinPoint) {
        logger.debug("Before {}", joinPoint.getSignature().toShortString());
    }

    @AfterReturning(pointcut = "applicationPackagePointcut()", returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.debug("AfterReturning {} -> {}", joinPoint.getSignature().toShortString(), result);
    }

    @AfterThrowing(pointcut = "applicationPackagePointcut()", throwing = "exception")
    public void logAfterThrowing(JoinPoint joinPoint, Throwable exception) {
        logger.warn("AfterThrowing {} -> {}", joinPoint.getSignature().toShortString(), exception.getMessage());
    }
}

