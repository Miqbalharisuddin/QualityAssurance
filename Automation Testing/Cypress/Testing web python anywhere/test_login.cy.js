describe('Login', () => {
    it('Successfull Login', () => {
        cy.visit('http://barru.pythonanywhere.com/daftar')
        cy.get('#email').type('jagoku@gmail.com')
        cy.get('#password').type('jago123')
        cy.get('#signin_login').click()
        cy.get('#swal2-content')
        cy.get('.swal2-confirm').click()

    })
    it('Failed Login blank field', () => {
        cy.visit('http://barru.pythonanywhere.com/daftar')
        cy.get('#email').type(' ')
        cy.get('#password').type(' ')
        cy.get('#signin_login').click()
        cy.get('#swal2-content')
        cy.get('.swal2-confirm').click()
    })
})
