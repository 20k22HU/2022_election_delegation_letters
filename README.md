### What is this?
It is a draft that should eventually do the following:

1. Take delegation data from Hasura >> GraphQL
2. Take a letter template by the legal team
3. Use the letter as Jinja template and generate letters using the delegation data

### What is missing?

- Currently, user data comes from a local json dummy file
- The LibreOffice pdf conversion is not coded
- Filename should start with numerical UID:OEVK-TEVK

### What is done?
- The Jinja template is functional
- The json traversing is functional
- The document generation is functional

### How does the LibreOffice pdf conversion work?
`$ lowriter --headless --convert-to pdf szszb_megbizo_OEVK02_Baranya_TEVK036_Boldogasszonyfalva.html`
