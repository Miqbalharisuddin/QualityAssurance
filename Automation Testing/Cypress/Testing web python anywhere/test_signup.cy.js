describe('Sign Up', () => {
    it('Successfull Sign Up', () => {
        cy.visit('http://barru.pythonanywhere.com/daftar')
        cy.get('#signUp').click()
        cy.get('#name_register').type('jago')
        cy.get('#email_register').type('jago@gmail.com')
        cy.get('#password_register').type('jago123')
        cy.get('#signup_register').click()
        cy.url().should('include', 'http://barru.pythonanywhere.com/daftar')

    })
    it('Failed Signup blank field', () => {
        cy.visit('http://barru.pythonanywhere.com/daftar')
        cy.get('#signUp').click()
        cy.get('#name_register').type(' ')
        cy.get('#email_register').type(' ')
        cy.get('#password_register').type(' ')
        cy.get('#signup_register').click()
        cy.get('#swal2-content')
        cy.get('.swal2-confirm').click()

    })
})