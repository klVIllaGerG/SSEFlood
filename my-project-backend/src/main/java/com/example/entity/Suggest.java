package com.example.entity;


import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Suggest {
    @Id
    private String category;
    private String suggestions;

    public Suggest() {
    }

    public Suggest(String category, String suggestions) {
        this.category = category;
        this.suggestions = suggestions;
    }

    // Getters and setters...
}