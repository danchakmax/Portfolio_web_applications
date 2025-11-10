// pages/dashboard.js
import { useEffect, useState } from "react";

export default function Dashboard() {
  const [heroes, setHeroes] = useState([]);
  const [aboutMe, setAboutMe] = useState([]);
  const [skills, setSkills] = useState([]);
  const [futurePlans, setFuturePlans] = useState([]);
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const heroesRes = await fetch("http://127.0.0.1:8000/api/heroes/");
        setHeroes(await heroesRes.json());

        const aboutRes = await fetch("http://127.0.0.1:8000/api/aboutme/");
        setAboutMe(await aboutRes.json());

        const skillsRes = await fetch("http://127.0.0.1:8000/api/skills/");
        setSkills(await skillsRes.json());

        const futureRes = await fetch("http://127.0.0.1:8000/api/futureplans/");
        setFuturePlans(await futureRes.json());

        const contactsRes = await fetch("http://127.0.0.1:8000/api/contacts/");
        setContacts(await contactsRes.json());
      } catch (err) {
        console.error("Error fetching data:", err);
      }
    };

    fetchData();
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Dashboard</h1>

      <section>
        <h2>Heroes</h2>
        <ul>
         {heroes.map(hero => (
  <li key={hero.id}>
    {hero.photo && <img src={hero.photo} alt={hero.name} style={{ width: '100px', height: '100px', objectFit: 'cover' }} />}
    {hero.name} – {hero.profession}
  </li>
))}
        </ul>
      </section>

      <section>
        <h2>About Me</h2>
        <ul>
          {aboutMe.map((item) => (
            <li key={item.id} style={{ marginBottom: "1rem" }}>
              {item.photo && (
                <img
                  src={item.photo}
                  alt={item.description}
                  style={{ width: "100px", height: "100px", objectFit: "cover", marginRight: "10px" }}
                />
              )}
              {item.description}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Skills</h2>
        <ul>
          {skills.map((skill) => (
            <li key={skill.id}>
              {skill.name} – Level: {skill.level}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Future Plans</h2>
        <ul>
          {futurePlans.map((plan) => (
            <li key={plan.id}>
              <strong>{plan.title}:</strong> {plan.description}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Contacts</h2>
        <ul>
          {contacts.map((contact) => (
            <li key={contact.id}>
              {contact.name} – {contact.email} – {contact.message}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
