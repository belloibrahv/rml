# System Architecture: AI-Powered Career Recommendation System

## High-Level System Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        A[Web Browser<br/>HTML/CSS/JavaScript]
        B[Mobile Browser<br/>Responsive Design]
    end
    
    subgraph "Presentation Layer"
        C[Flask Web Server<br/>Port 5001]
        D[Static Files<br/>CSS/JS/Assets]
        E[HTML Templates<br/>Jinja2 Engine]
    end
    
    subgraph "Application Layer"
        F[Career Recommendation Engine<br/>Rule-based AI]
        G[User Input Processor<br/>Validation & Sanitization]
        H[Career Database Manager<br/>18 Careers, 6 Industries]
        I[Education Level Matcher<br/>5 Education Levels]
        J[Confidence Calculator<br/>Scoring Algorithm]
    end
    
    subgraph "Data Layer"
        K[SQLite Database<br/>career_reco.db]
        L[Career Database<br/>In-Memory Dictionary]
        M[User Recommendations<br/>Analytics Data]
    end
    
    subgraph "External Components"
        N[Python Virtual Environment<br/>Dependencies Management]
        O[Installation Scripts<br/>install.bat/install.sh]
        P[Startup Scripts<br/>start.bat/start.sh]
    end
    
    %% Client to Presentation Layer
    A --> C
    B --> C
    C --> D
    C --> E
    
    %% Presentation to Application Layer
    C --> F
    C --> G
    G --> F
    F --> H
    F --> I
    F --> J
    
    %% Application to Data Layer
    H --> L
    F --> K
    K --> M
    
    %% External Components
    N --> C
    O --> N
    P --> C
    
    %% Styling
    classDef clientLayer fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef presentationLayer fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef applicationLayer fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef dataLayer fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef externalLayer fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    
    class A,B clientLayer
    class C,D,E presentationLayer
    class F,G,H,I,J applicationLayer
    class K,L,M dataLayer
    class N,O,P externalLayer
```

## Detailed Component Architecture

```mermaid
graph LR
    subgraph "Frontend Components"
        A1[Landing Page<br/>index.html]
        A2[Recommendation Form<br/>recommend.html]
        A3[About Page<br/>about.html]
        A4[CSS Styling<br/>style.css]
        A5[JavaScript Logic<br/>main.js]
    end
    
    subgraph "Backend Services"
        B1[Flask Application<br/>app.py]
        B2[Route Handlers<br/>API Endpoints]
        B3[Template Engine<br/>Jinja2]
        B4[Static File Server<br/>CSS/JS/Assets]
    end
    
    subgraph "Business Logic"
        C1[Career Recommendation Engine<br/>Rule-based Algorithm]
        C2[Input Validation<br/>Data Sanitization]
        C3[Education Level Mapping<br/>Normalization]
        C4[Confidence Scoring<br/>Algorithm]
        C5[Alternative Career Generator<br/>Fallback Logic]
    end
    
    subgraph "Data Management"
        D1[Career Database<br/>18 Career Profiles]
        D2[Industry Classification<br/>6 Industries]
        D3[Education Requirements<br/>5 Levels]
        D4[SQLite Database<br/>User Analytics]
        D5[Recommendation History<br/>Storage]
    end
    
    subgraph "System Utilities"
        E1[Installation Scripts<br/>Cross-platform]
        E2[Startup Scripts<br/>Environment Setup]
        E3[Error Handling<br/>Logging System]
        E4[Configuration Management<br/>Settings]
    end
    
    %% Frontend to Backend
    A1 --> B1
    A2 --> B1
    A3 --> B1
    A4 --> B4
    A5 --> B4
    
    %% Backend to Business Logic
    B1 --> B2
    B2 --> C1
    B2 --> C2
    C1 --> C3
    C1 --> C4
    C1 --> C5
    
    %% Business Logic to Data
    C1 --> D1
    C1 --> D2
    C1 --> D3
    C1 --> D4
    C1 --> D5
    
    %% System Utilities
    E1 --> B1
    E2 --> B1
    E3 --> B1
    E4 --> B1
    
    %% Styling
    classDef frontend fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef backend fill:#f1f8e9,stroke:#33691e,stroke-width:2px
    classDef business fill:#fff8e1,stroke:#f57f17,stroke-width:2px
    classDef data fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    classDef utils fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px
    
    class A1,A2,A3,A4,A5 frontend
    class B1,B2,B3,B4 backend
    class C1,C2,C3,C4,C5 business
    class D1,D2,D3,D4,D5 data
    class E1,E2,E3,E4 utils
```

## Data Flow Architecture

```mermaid
sequenceDiagram
    participant U as User
    participant B as Browser
    participant F as Flask Server
    participant E as Recommendation Engine
    participant D as Database
    participant C as Career DB
    
    U->>B: Fill Career Form
    B->>F: POST /api/recommend
    F->>F: Validate Input Data
    
    F->>E: Process Recommendation Request
    E->>C: Query Career Database
    C->>E: Return Career Profiles
    
    E->>E: Apply Rule-based Algorithm
    E->>E: Match Skills & Interests
    E->>E: Check Education Compatibility
    E->>E: Calculate Confidence Score
    E->>E: Generate Alternatives
    
    E->>D: Store Recommendation
    D->>E: Confirm Storage
    
    E->>F: Return Recommendation Results
    F->>B: JSON Response
    B->>U: Display Results
    
    Note over E: Rule-based AI Engine<br/>- Skill Matching<br/>- Interest Alignment<br/>- Education Compatibility<br/>- Industry Preference<br/>- Fallback Logic
```

## Technology Stack Architecture

```mermaid
graph TB
    subgraph "Frontend Technologies"
        A1[HTML5<br/>Semantic Markup]
        A2[CSS3<br/>Responsive Design]
        A3[JavaScript<br/>ES6+ Features]
        A4[Bootstrap-like Styling<br/>Custom CSS Framework]
    end
    
    subgraph "Backend Technologies"
        B1[Python 3.11<br/>Core Language]
        B2[Flask Framework<br/>Web Framework]
        B3[Jinja2<br/>Template Engine]
        B4[SQLite3<br/>Database Engine]
        B5[Virtual Environment<br/>venv]
    end
    
    subgraph "Development Tools"
        C1[Git<br/>Version Control]
        C2[GitHub<br/>Repository Hosting]
        C3[Command Line<br/>CLI Tools]
        C4[Batch Scripts<br/>Windows Automation]
        C5[Shell Scripts<br/>Unix Automation]
    end
    
    subgraph "System Requirements"
        D1[Windows 10/11<br/>Operating System]
        D2[Python 3.8+<br/>Runtime Environment]
        D3[Web Browser<br/>Chrome/Edge/Firefox]
        D4[Internet Connection<br/>Initial Setup]
        D5[Command Prompt<br/>Terminal Access]
    end
    
    %% Frontend Stack
    A1 --> A2
    A2 --> A3
    A3 --> A4
    
    %% Backend Stack
    B1 --> B2
    B2 --> B3
    B2 --> B4
    B1 --> B5
    
    %% Development Tools
    C1 --> C2
    C3 --> C4
    C3 --> C5
    
    %% System Requirements
    D1 --> D2
    D2 --> D3
    D3 --> D4
    D4 --> D5
    
    %% Cross-stack connections
    A4 --> B2
    B2 --> C1
    C4 --> D1
    C5 --> D1
    
    %% Styling
    classDef frontend fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef backend fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef devtools fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef requirements fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A1,A2,A3,A4 frontend
    class B1,B2,B3,B4,B5 backend
    class C1,C2,C3,C4,C5 devtools
    class D1,D2,D3,D4,D5 requirements
```

## Career Recommendation Algorithm Flow

```mermaid
flowchart TD
    A[User Input<br/>Skills, Interests, Education, Industry] --> B{Validate Input}
    B -->|Invalid| C[Return Error Message]
    B -->|Valid| D[Process Input Data]
    
    D --> E[Check Skills Against Career Database]
    E --> F{Skills Match Found?}
    F -->|Yes| G[Filter by Education Level]
    F -->|No| H[Check Interests Against Career Database]
    
    H --> I{Interests Match Found?}
    I -->|Yes| G
    I -->|No| J[Check Preferred Industry]
    
    J --> K{Industry Specified?}
    K -->|Yes| L[Get Careers from Industry]
    K -->|No| M[Use Default Careers by Education]
    
    L --> G
    M --> G
    
    G --> N{Education Compatible Careers?}
    N -->|Yes| O[Select Primary Career]
    N -->|No| P[Use Fallback Logic]
    
    P --> Q[Find Any Suitable Career]
    Q --> O
    
    O --> R[Generate Alternative Careers]
    R --> S[Calculate Confidence Score]
    S --> T[Prepare Response]
    T --> U[Return Recommendation Results]
    
    C --> U
    
    %% Styling
    classDef input fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef process fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef decision fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef output fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A input
    class D,E,G,H,J,L,M,O,P,Q,R,S,T process
    class B,F,I,K,N decision
    class C,U output
```

## Database Schema Architecture

```mermaid
erDiagram
    RECOMMENDATIONS {
        int id PK
        string name
        string email
        string education_level
        text skills
        text interests
        string preferred_industry
        string recommended_career
        float confidence_score
        text alternative_careers
        datetime created_at
    }
    
    CAREER_DATABASE {
        string career_name PK
        string industry
        array education_requirements
        string description
        array required_skills
        string salary_range
        string growth_potential
    }
    
    INDUSTRIES {
        string industry_name PK
        array careers
        string description
    }
    
    EDUCATION_LEVELS {
        string level_name PK
        array compatible_careers
        string description
    }
    
    RECOMMENDATIONS ||--o{ CAREER_DATABASE : "references"
    CAREER_DATABASE ||--o{ INDUSTRIES : "belongs_to"
    CAREER_DATABASE ||--o{ EDUCATION_LEVELS : "requires"
```

## Deployment Architecture

```mermaid
graph TB
    subgraph "Development Environment"
        A1[Local Machine<br/>Windows/macOS/Linux]
        A2[Python Virtual Environment<br/>venv]
        A3[Flask Development Server<br/>localhost:5001]
        A4[SQLite Database<br/>Local File]
    end
    
    subgraph "Production Environment"
        B1[Web Server<br/>Apache/Nginx]
        B2[WSGI Server<br/>Gunicorn/uWSGI]
        B3[Flask Application<br/>Production Mode]
        B4[Production Database<br/>PostgreSQL/MySQL]
        B5[Load Balancer<br/>Optional]
    end
    
    subgraph "Cloud Deployment"
        C1[Heroku Platform<br/>PaaS]
        C2[AWS/GCP/Azure<br/>IaaS]
        C3[Docker Containers<br/>Containerization]
        C4[CI/CD Pipeline<br/>GitHub Actions]
    end
    
    subgraph "Monitoring & Logging"
        D1[Application Logs<br/>Structured Logging]
        D2[Performance Monitoring<br/>Metrics Collection]
        D3[Error Tracking<br/>Exception Handling]
        D4[Health Checks<br/>Endpoint Monitoring]
    end
    
    %% Development Flow
    A1 --> A2
    A2 --> A3
    A3 --> A4
    
    %% Production Flow
    B1 --> B2
    B2 --> B3
    B3 --> B4
    B5 --> B1
    
    %% Cloud Deployment
    C1 --> B3
    C2 --> B3
    C3 --> B3
    C4 --> C1
    
    %% Monitoring
    D1 --> B3
    D2 --> B3
    D3 --> B3
    D4 --> B3
    
    %% Styling
    classDef dev fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef prod fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef cloud fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef monitoring fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A1,A2,A3,A4 dev
    class B1,B2,B3,B4,B5 prod
    class C1,C2,C3,C4 cloud
    class D1,D2,D3,D4 monitoring
```

## Security Architecture

```mermaid
graph TB
    subgraph "Input Validation Layer"
        A1[Data Sanitization<br/>XSS Prevention]
        A2[Input Validation<br/>Type Checking]
        A3[SQL Injection Prevention<br/>Parameterized Queries]
    end
    
    subgraph "Application Security"
        B1[Error Handling<br/>Information Disclosure Prevention]
        B2[Rate Limiting<br/>DDoS Protection]
        B3[Session Management<br/>Secure Cookies]
    end
    
    subgraph "Data Security"
        C1[Data Encryption<br/>At Rest & In Transit]
        C2[Access Control<br/>User Permissions]
        C3[Audit Logging<br/>Security Events]
    end
    
    subgraph "Infrastructure Security"
        D1[HTTPS/SSL<br/>Encrypted Communication]
        D2[Firewall Rules<br/>Network Security]
        D3[Regular Updates<br/>Security Patches]
    end
    
    %% Security Flow
    A1 --> A2
    A2 --> A3
    A3 --> B1
    B1 --> B2
    B2 --> B3
    B3 --> C1
    C1 --> C2
    C2 --> C3
    C3 --> D1
    D1 --> D2
    D2 --> D3
    
    %% Styling
    classDef input fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef app fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef data fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef infra fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A1,A2,A3 input
    class B1,B2,B3 app
    class C1,C2,C3 data
    class D1,D2,D3 infra
```

## Performance Architecture

```mermaid
graph LR
    subgraph "Caching Layer"
        A1[In-Memory Caching<br/>Career Database]
        A2[Response Caching<br/>Static Content]
        A3[Database Query Caching<br/>Recommendations]
    end
    
    subgraph "Optimization Techniques"
        B1[Database Indexing<br/>Query Optimization]
        B2[Static File Compression<br/>Gzip/Brotli]
        B3[Minification<br/>CSS/JS Optimization]
        B4[Image Optimization<br/>WebP Format]
    end
    
    subgraph "Scalability Features"
        C1[Horizontal Scaling<br/>Load Balancing]
        C2[Vertical Scaling<br/>Resource Allocation]
        C3[Database Scaling<br/>Read Replicas]
        C4[CDN Integration<br/>Content Delivery]
    end
    
    subgraph "Monitoring & Metrics"
        D1[Response Time Monitoring<br/>Performance Tracking]
        D2[Resource Usage Monitoring<br/>CPU/Memory/Disk]
        D3[Error Rate Monitoring<br/>Reliability Metrics]
        D4[User Experience Metrics<br/>Page Load Times]
    end
    
    %% Performance Flow
    A1 --> B1
    A2 --> B2
    A3 --> B3
    B1 --> C1
    B2 --> C2
    B3 --> C3
    C1 --> D1
    C2 --> D2
    C3 --> D3
    C4 --> D4
    
    %% Styling
    classDef cache fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef optimization fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef scalability fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef monitoring fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    
    class A1,A2,A3 cache
    class B1,B2,B3,B4 optimization
    class C1,C2,C3,C4 scalability
    class D1,D2,D3,D4 monitoring
```

---

## Architecture Summary

### Key Architectural Components:

1. **Frontend Layer**: HTML5, CSS3, JavaScript with responsive design
2. **Backend Layer**: Flask web framework with Python 3.11
3. **Business Logic Layer**: Rule-based AI recommendation engine
4. **Data Layer**: SQLite database with in-memory career database
5. **Deployment Layer**: Cross-platform installation and startup scripts

### Architectural Patterns:

1. **MVC Pattern**: Model (Career Database), View (HTML Templates), Controller (Flask Routes)
2. **Layered Architecture**: Clear separation between presentation, business logic, and data layers
3. **Rule-based AI**: Deterministic recommendation algorithm with fallback logic
4. **RESTful API**: Standard HTTP endpoints for data exchange

### Scalability Considerations:

1. **Horizontal Scaling**: Stateless application design
2. **Database Optimization**: Indexed queries and caching strategies
3. **Performance Monitoring**: Response time and resource usage tracking
4. **Security Measures**: Input validation, error handling, and data sanitization

This architecture provides a robust, scalable, and maintainable foundation for the AI Career Recommendation System while ensuring ease of deployment and use for end users. 