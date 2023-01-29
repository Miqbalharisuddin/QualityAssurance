describe('Make Appointment', () => {
    it('Successfull Make Appointment', () => {
        cy.visit('https://katalon-demo-cura.herokuapp.com/')
        cy.get('#menu-toggle > .fa').click()
        cy.get('.sidebar-nav > :nth-child(4) > a').click()
        cy.get('#txt-username').type('John Doe')
        cy.get('#txt-password').type('ThisIsNotAPassword')
        cy.get('#btn-login').click()
        cy.wait(1000)
        cy.get('#combo_facility').select('Hongkong CURA Healthcare Center')
        cy.get('.checkbox-inline').click()
        cy.get('.col-sm-4 > :nth-child(2)').click()
        cy.get('.glyphicon').click()
        cy.get('tbody > :nth-child(3) > :nth-child(5)').click()
        cy.get('.glyphicon').click()
        cy.get('#btn-book-appointment').click()
        cy.url().should('include', 'https://katalon-demo-cura.herokuapp.com/appointment.php#summary')


    })
})